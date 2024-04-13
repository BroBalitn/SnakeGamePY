import pygame
import Model.SnakeModel as SnakeModel
import Model.BodyModel as BodyModel
import Model.ButtonModel as ButtonModel
import Controller.BodyController as BodyController
import Controller.MoveController as MoveController
import Controller.AppleController as AppleController
import Controller.CollideController as CollideController
import Controller.ScoreController as ScoreController
from datetime import datetime
from pygame.locals import *
from pygame import mixer

def main():
    pygame.init()
    #Display -----------------------------------------------------------------------------------
    WIDTH, HEIGHT = 300,300
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Snake Game")
    clk = pygame.time.Clock()
    #MenuTextures -------------------------------------------------------------------------------
    menuimg = pygame.image.load('img/menu.png').convert()
    singleimg = pygame.image.load('img/egyjatekos.png').convert_alpha()
    multiimg = pygame.image.load('img/tobbjatekos.png').convert_alpha()
    leaderboardimg = pygame.image.load('img/dicsosegtabla.png').convert_alpha()
    exitimg = pygame.image.load('img/kilepes.png').convert_alpha()
    #GameTextures ------------------------------------------------------------------------------
    map = pygame.image.load('img/palya.png').convert()
    apple = pygame.image.load('img/alma.png').convert_alpha()
    snake = pygame.image.load('img/kigyo.png').convert_alpha()
    snakebody = pygame.image.load('img/kigyotest.png').convert()
    snake2 = pygame.image.load('img/kigyo2.png').convert_alpha()
    snake2body = pygame.image.load('img/kigyo2test.png').convert()
    #GameOverTextures --------------------------------------------------------------------------
    gameoverbackg = pygame.image.load('img/vege.png').convert()
    newgame = pygame.image.load('img/ujjatek.png').convert_alpha()
    mainmenu = pygame.image.load('img/fooldal.png').convert_alpha()
    #LeaderboardTextures -----------------------------------------------------------------------
    leaderboardbackg = pygame.image.load('img/dicsosegtablabc.png').convert()
    back = pygame.image.load('img/vissza.png').convert_alpha()
    #MenuButtons -------------------------------------------------------------------------------
    singlebtn = ButtonModel.Button(100,100,singleimg)
    multibtn = ButtonModel.Button(100,150,multiimg)
    leaderboardbtn = ButtonModel.Button(100,200,leaderboardimg)
    exitbtn = ButtonModel.Button(100,250,exitimg)
    #GameOverButtons ---------------------------------------------------------------------------
    newgamebtn = ButtonModel.Button(110,180,newgame)
    mainmenubtn = ButtonModel.Button(110,230,mainmenu)
    #LeadeboardButton --------------------------------------------------------------------------
    backbtn = ButtonModel.Button(100,250,back)
    #Game Variables ----------------------------------------------------------------------------
    positions = [[100,120],[100,140],[100,160],[100,180],[100,200]]
    positions2 = [[200,120],[200,140],[200,160],[200,180],[200,200]]
    playerlook = 0 #0-fel, 1-le, 2-bal, 3-jobb
    playerlook2 = 0 #0-fel, 1-le, 2-bal, 3-jobb
    player = SnakeModel.Snake(positions,snake,playerlook)
    player2 = SnakeModel.Snake(positions2,snake2,playerlook2)
    applespawn = True
    applepos = []
    score = 0
    running = True
    delaystart = 0
    menu = 0 # 0 = menü, 1 = egyjátékos, 2 = kétjátékos, 3 = Dicsőségtábla, 4 = vége
    played = 0 #0 = egyjátékos, 1 = többjátékos
    font = pygame.font.Font('PRISTINA.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf',20)
    singlescores = []
    multiscores = []
    mixer.init()
    mixer.music.load('hatterzene.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    #Running ------------------------------------------------------------------------------------
    while running:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        if menu == 0:
            screen.blit(menuimg,(0,0))
            if singlebtn.btnpush(screen):
                menu = 1
            if multibtn.btnpush(screen):
                menu = 2
            if leaderboardbtn.btnpush(screen):
                menu = 3
            if exitbtn.btnpush(screen):
                break
        elif menu == 1:
            screen.blit(map, (0,0))
            if delaystart == 8:
                player = MoveController.inputdir(player)
                player = MoveController.bodyfollow(player,screen,snakebody)
                player = MoveController.movement(player)
                if applespawn:
                    applepos = AppleController.applegen(player)
                    applespawn = False
                screen.blit(apple,(applepos[0],applepos[1]))
                bodygrow = BodyModel.BodyReturn(player,applepos,score,applespawn)
                bodygrow = BodyController.bodygrow(bodygrow)
                player = bodygrow.player
                applepos = bodygrow.applepos
                score = bodygrow.score
                applespawn = bodygrow.applespawn
                screen.blit(player.snake, (player.positions[0][0],player.positions[0][1]))
                if CollideController.wallcollide(player) or CollideController.bodycollide(player):
                    menu = 4
                    currrendate = datetime.now()
                    currenttime = currrendate.strftime("%Y.%m.%d.")
                    writescore = open('egyleaderboard.txt','a')
                    if score < 10 : writescore.write(f"\n{currenttime} --- 00{score}")
                    elif score < 100 : writescore.write(f"\n{currenttime} --- 0{score}")
                    elif score > 99 : writescore.write(f"\n{currenttime} --- {score}")
                    writescore.close()
            else:
                delaystart += 1
        elif menu == 2:
            screen.blit(map, (0,0))
            if delaystart == 8:
                player = MoveController.inputdir(player)
                player = MoveController.bodyfollow(player,screen,snakebody)
                player = MoveController.movement(player)
                player2 = MoveController.multiinputdir(player2)
                player2 = MoveController.bodyfollow(player2,screen,snake2body)
                player2 = MoveController.movement(player2)
                if applespawn:
                    applepos = AppleController.applegen(player,player2)
                    applespawn = False
                screen.blit(apple,(applepos[0],applepos[1]))
                bodygrow = BodyModel.BodyReturn(player,applepos,score,applespawn)
                bodygrow = BodyController.bodygrow(bodygrow)
                player = bodygrow.player
                applepos = bodygrow.applepos
                score = bodygrow.score
                applespawn = bodygrow.applespawn
                bodygrow2 = BodyModel.BodyReturn(player2,applepos,score,applespawn)
                bodygrow2 = BodyController.bodygrow(bodygrow2)
                player2 = bodygrow2.player
                applepos = bodygrow2.applepos
                score = bodygrow2.score
                applespawn = bodygrow2.applespawn
                screen.blit(player.snake, (player.positions[0][0],player.positions[0][1]))
                screen.blit(player2.snake, (player2.positions[0][0],player2.positions[0][1]))
                if CollideController.wallcollide(player) or CollideController.bodycollide(player):
                    menu = 4
                    played = 1
                    currrendate = datetime.now()
                    currenttime = currrendate.strftime("%Y.%m.%d.")
                    writescore = open('tobbleaderboard.txt','a')
                    if score < 10 : writescore.write(f"\n{currenttime} --- 00{score}")
                    elif score < 100 : writescore.write(f"\n{currenttime} --- 0{score}")
                    elif score > 99 : writescore.write(f"\n{currenttime} --- {score}")
                    writescore.close()
                if CollideController.wallcollide(player2) or CollideController.bodycollide(player2):
                    menu = 4
                    played = 1
                    currrendate = datetime.now()
                    currenttime = currrendate.strftime("%Y.%m.%d.")
                    writescore = open('tobbleaderboard.txt','a')
                    if score < 10 : writescore.write(f"\n{currenttime} --- 00{score}")
                    elif score < 100 : writescore.write(f"\n{currenttime} --- 0{score}")
                    elif score > 99 : writescore.write(f"\n{currenttime} --- {score}")
                    writescore.close()
                if CollideController.playercollide(player,player2):
                    menu = 4
                    played = 1
                    currrendate = datetime.now()
                    currenttime = currrendate.strftime("%Y.%m.%d.")
                    writescore = open('tobbleaderboard.txt','a')
                    if score < 10 : writescore.write(f"\n{currenttime} --- 00{score}")
                    elif score < 100 : writescore.write(f"\n{currenttime} --- 0{score}")
                    elif score > 99 : writescore.write(f"\n{currenttime} --- {score}")
                    writescore.close()
            else:
                delaystart += 1
        elif menu == 3:
            screen.blit(leaderboardbackg, (0,0))
            singlescores = ScoreController.scoreblit(singlescores,screen,font2)
            multiscores = ScoreController.multiscoreblit(multiscores,screen,font2)
            singlescores = []
            multiscores = []
            if backbtn.btnpush(screen):
                menu = 0
        elif menu == 4:
            screen.blit(gameoverbackg,(0,0))
            text = font.render(f"Elért pont: {score}", True, (255,255,255))
            screen.blit(text,(90,130))
            if newgamebtn.btnpush(screen):
                if played == 0:
                    menu = 1
                    #Game Variables -----------------------------------------------------------
                    delaystart = 0
                    played = 0
                    positions = [[100,120],[100,140],[100,160],[100,180],[100,200]]
                    positions2 = [[200,120],[200,140],[200,160],[200,180],[200,200]]
                    playerlook = 0 #0-fel, 1-le, 2-bal, 3-jobb
                    playerlook2 = 0 #0-fel, 1-le, 2-bal, 3-jobb
                    player = SnakeModel.Snake(positions,snake,playerlook)
                    player2 = SnakeModel.Snake(positions2,snake2,playerlook2)
                    applespawn = True
                    applepos = []
                    score = 0
                else:
                    menu = 2
                    #Game Variables -----------------------------------------------------------
                    delaystart = 0
                    played = 0
                    positions = [[100,120],[100,140],[100,160],[100,180],[100,200]]
                    positions2 = [[200,120],[200,140],[200,160],[200,180],[200,200]]
                    playerlook = 0 #0-fel, 1-le, 2-bal, 3-jobb
                    playerlook2 = 0 #0-fel, 1-le, 2-bal, 3-jobb
                    player = SnakeModel.Snake(positions,snake,playerlook)
                    player2 = SnakeModel.Snake(positions2,snake2,playerlook2)
                    applespawn = True
                    applepos = []
                    score = 0
            if mainmenubtn.btnpush(screen):
                menu = 0
                #Game Variables -----------------------------------------------------------
                delaystart = 0
                played = 0
                positions = [[100,120],[100,140],[100,160],[100,180],[100,200]]
                positions2 = [[200,120],[200,140],[200,160],[200,180],[200,200]]
                playerlook = 0 #0-fel, 1-le, 2-bal, 3-jobb
                playerlook2 = 0 #0-fel, 1-le, 2-bal, 3-jobb
                player = SnakeModel.Snake(positions,snake,playerlook)
                player2 = SnakeModel.Snake(positions2,snake2,playerlook2)
                applespawn = True
                applepos = []
                score = 0
        pygame.display.update()
        clk.tick(8)
    pygame.quit()

main()