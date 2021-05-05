import pygame

WIDTH = 1000
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


fonttext = pygame.font.SysFont("opensans", 80)
font = pygame.font.SysFont("opensans", 100)
fontsmall = pygame.font.SysFont("opensans", 65)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    teamname1 = "Ospel"
    teamname2 = "Maaseik"
    teamscore1 = str(0)
    teamscore2 = str(0)
    teamgame1 = str(0)
    teamgame2 = str(0)
    
    team1 = fonttext.render(teamname1, True, "#EB5E0C")
    screen.blit(team1, (75, 300))
    team2 = fonttext.render(teamname2, True, "#EB5E0C")
    screen.blit(team2, (690, 300))


    teamnumber1 = font.render(teamscore1, True, "white")
    screen.blit(teamnumber1, (150, 450))
    teamnumber2 = font.render(teamscore2, True, "white")
    screen.blit(teamnumber2, (800, 450))

    teamset1 = fontsmall.render(teamgame1, True, "white")
    screen.blit(teamset1, (250, 450))
    teamset2 = fontsmall.render(teamgame2, True, "white")
    screen.blit(teamset2, (700, 450))

    pygame.display.flip()
