import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# TODO: Laad hier je font
# font = ...

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    label = "Hallo"
    # TODO: Render hier de tekst en toon op het scherm
    # text = ...
    # ...

    pygame.display.flip()
