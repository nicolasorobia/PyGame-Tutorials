import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") # Configure title of game window
pygame.display.set_icon(pygame.image.load('images\player.png')) # Configure icon image next to title
running = True

# plain surface
# surf = pygame.Surface((100,100))
# surf.fill('orange')

# importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) ) for _ in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('darkgray')
    display_surface.blit(player_surf, ((1280/2) - (player_surf.get_width()/2), 310))

    # place 20 stars surfaces randomly
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    pygame.display.update()

pygame.quit()
