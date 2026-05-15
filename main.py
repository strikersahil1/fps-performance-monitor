import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

running = True

while running:
    screen.fill((20, 20, 20))

    fps = int(clock.get_fps())

    fps_text = font.render(f"FPS: {fps}", True, (0, 255, 0))
    screen.blit(fps_text, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    clock.tick(60)

pygame.quit()