import pygame

pygame.init()
pygame.display.set_mode((800, 600))
pygame.display.toggle_fullscreen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
