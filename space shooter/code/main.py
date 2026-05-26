import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.display.set_icon(pygame.image.load('images/player.png'))
running = True

# surface
surf = pygame.Surface((100,100))
surf.fill('orange')

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    display_surface.fill('darkgray')
    display_surface.blit(surf, (640, 360))
    pygame.display.update()

pygame.quit()
