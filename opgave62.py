import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# TODO: Laad hier je font
font = pygame.font.SysFont("montserrat", 32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    teamname1 = "Ospel"
    teamname2 = "Maaseik"
    # TODO: Render hier de tekst en toon op het scherm
    team1 = font.render(teamname1, True, "#EB5E0C")
    screen.blit(team1, (0, 0))

    team2 = font.render(teamname2, True, "#EB5E0C")
    screen.blit(team2, (400, 200))

    pygame.display.flip()
