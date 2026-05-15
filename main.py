import pygame
import psutil
import win32gui
import win32con

pygame.init()

WIDTH, HEIGHT = 260, 140

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.NOFRAME
)

hwnd = pygame.display.get_wm_info()["window"]

win32gui.SetWindowPos(
    hwnd,
    win32con.HWND_TOPMOST,
    100,
    100,
    0,
    0,
    win32con.SWP_NOSIZE
)

font = pygame.font.SysFont("Arial", 32)
small_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

running = True

cpu = 0

dragging = False
offset_x = 0
offset_y = 0

while running:

    screen.fill((20, 20, 20))

    fps = int(clock.get_fps())

    # Update CPU every ~0.5 sec
    if pygame.time.get_ticks() % 500 < 16:
        cpu = psutil.cpu_percent(interval=None)

    ram = psutil.virtual_memory().percent

    fps_text = font.render(f"FPS: {fps}", True, (0, 255, 0))
    cpu_text = small_font.render(f"CPU: {cpu}%", True, (255, 255, 255))
    ram_text = small_font.render(f"RAM: {ram}%", True, (255, 255, 255))
    close_text = small_font.render("X", True, (255, 80, 80))

    screen.blit(close_text, (230, 10))
    screen.blit(fps_text, (20, 15))
    screen.blit(cpu_text, (20, 60))
    screen.blit(ram_text, (20, 90))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Close button
            if 230 <= mouse_x <= 250 and 10 <= mouse_y <= 35:
                running = False

            dragging = True

            rect = win32gui.GetWindowRect(hwnd)

            offset_x = rect[0] - mouse_x
            offset_y = rect[1] - mouse_y

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    if dragging:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            mouse_x + offset_x,
            mouse_y + offset_y,
            0,
            0,
            win32con.SWP_NOSIZE
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()