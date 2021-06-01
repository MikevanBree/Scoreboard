import pygame
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

HEIGHT = config["DEFAULT"].getint("Height")
WIDTH = config["DEFAULT"].getint("Width")

# definitions Teams
teamname1 = config["TeamA"]["naam"]
teamname2 = config["TeamB"]["naam"]
teamscore1 = 0
teamscore2 = 0
teamgame1 = 0
teamgame2 = 0

# max rounds per set
set_score = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# fonts
fonttext = pygame.font.SysFont("verdana", 80)
font = pygame.font.SysFont("verdana", 100)
fontsmall = pygame.font.SysFont("verdana", 65)

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
    image1 = pygame.image.load(config["TeamA"]["Logo"])
    image1 = pygame.transform.scale(image1, (300, 175))
    screen.blit(image1, (33, 80))
    image2 = pygame.image.load(config["TeamB"]["Logo"])
    image2 = pygame.transform.scale(image2, (200, 200))
    screen.blit(image2, (700, 60))

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
