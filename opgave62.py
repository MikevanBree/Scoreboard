import pygame
import configparser
import time

config = configparser.ConfigParser()
config.read("config.ini")

HEIGHT = config["DEFAULT"].getint("height")
WIDTH = config["DEFAULT"].getint("width")

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
fontname = pygame.font.SysFont("verdana", 30)
fontrounds = pygame.font.Font("CursedTimerUlil-Aznm.ttf", 130)
fontsets = pygame.font.Font("CursedTimerUlil-Aznm.ttf", 65)
fonttimer = pygame.font.Font("CursedTimerUlil-Aznm.ttf", 50)

passed_time = 0
timer_started = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    start_time = pygame.time.get_ticks()
            elif event.key == pygame.K_r:
                teamscore1 = 0
                teamscore2 = 0
                teamgame1 = 0
                teamgame2 = 0
                set_score = 5
                print("Time stopped at:")
                print(passed_time)
                timer_started = False
                passed_time = 0
            elif event.key == pygame.K_LEFT:
                if timer_started:
                    teamscore1 = teamscore1 + 1
            elif event.key == pygame.K_RIGHT:
                if timer_started:
                    teamscore2 = teamscore2 + 1
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time
    
    if teamscore1 >= set_score:
        teamscore1 = 0
        teamscore2 = 0
        teamgame1 = teamgame1 + 1
    if teamscore2 >= set_score:
        teamscore2 = 0
        teamscore1 = 0
        teamgame2 = teamgame2 + 1

    screen.fill("black")

    # background render
    background = pygame.image.load(config["DEFAULT"]["background"])
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    # timer render
    timer = fonttimer.render(str(passed_time/1000), True, "yellow")
    screen.blit(timer, (430, 165))
    
    # Teamnames render
    team1 = fontname.render(teamname1, True, "#EB5E0C")
    screen.blit(team1, (150, 310))
    team2 = fontname.render(teamname2, True, "#EB5E0C")
    screen.blit(team2, (725, 310))

    # Teamlogo's render
    image1 = pygame.image.load(config["TeamA"]["Logo"])
    image1 = pygame.transform.smoothscale(image1, (200, 200))
    screen.blit(image1, (100, 80))
    image2 = pygame.image.load(config["TeamB"]["Logo"])
    image2 = pygame.transform.smoothscale(image2, (200, 200))
    screen.blit(image2, (700, 80))

    # Teamrounds render
    teamnumber1 = fontrounds.render(str(teamscore1), True, "white")
    screen.blit(teamnumber1, (150, 450))
    teamnumber2 = fontrounds.render(str(teamscore2), True, "white")
    screen.blit(teamnumber2, (800, 450))

    #Team sets render
    teamset1 = fontsets.render(str(teamgame1), True, "white")
    screen.blit(teamset1, (410, 375))
    teamset2 = fontsets.render(str(teamgame2), True, "white")
    screen.blit(teamset2, (575, 375))

    pygame.display.flip()
