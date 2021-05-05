import pygame

WIDTH = 1000
HEIGHT = 600

# definitions Teams
teamname1 = "Stokkem"
teamname2 = "Maaseik"
teamscore1 = 0
teamscore2 = 0
teamgame1 = 0
teamgame2 = 0

# max rounds per set
set_score = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# fonts
fonttext = pygame.font.SysFont("opensans", 80)
font = pygame.font.SysFont("opensans", 100)
fontsmall = pygame.font.SysFont("opensans", 65)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                teamscore1 = 0
                teamscore2 = 0
                teamgame1 = 0
                teamgame2 = 0
                set_score = 5
            elif event.key == pygame.K_RIGHT:
                teamscore1 = teamscore1 + 1
            elif event.key == pygame.K_LEFT:
                teamscore2 = teamscore2 + 1
    
    if teamscore1 >= set_score:
        teamscore1 = 0
        teamgame1 = teamgame1 + 1
    if teamscore2 >= set_score:
        teamscore2 = 0
        teamgame2 = teamgame2 + 1

    screen.fill("black")


    
    # Teamnames render
    team1 = fonttext.render(teamname1, True, "#EB5E0C")
    screen.blit(team1, (75, 300))
    team2 = fonttext.render(teamname2, True, "#EB5E0C")
    screen.blit(team2, (690, 300))

    # Teamlogo's render
    imageStokkem = pygame.image.load(r'.\images\logo dilen-stokkem.png')
    imageStokkem = pygame.transform.scale(imageStokkem, (300, 175))
    screen.blit(imageStokkem, (33, 80))
    imageMaaseik = pygame.image.load(r'.\images\logo maaseik.png')
    imageMaaseik = pygame.transform.scale(imageMaaseik, (200, 200))
    screen.blit(imageMaaseik, (700, 60))

    # Teamrounds render
    teamnumber1 = font.render(str(teamscore1), True, "white")
    screen.blit(teamnumber1, (150, 450))
    teamnumber2 = font.render(str(teamscore2), True, "white")
    screen.blit(teamnumber2, (800, 450))

    #Team sets render
    teamset1 = fontsmall.render(str(teamgame1), True, "white")
    screen.blit(teamset1, (250, 450))
    teamset2 = fontsmall.render(str(teamgame2), True, "white")
    screen.blit(teamset2, (700, 450))

    pygame.display.flip()
