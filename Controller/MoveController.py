import pygame

def inputdir(player):
    control = pygame.key.get_pressed()
    if control[pygame.K_UP] and player.playerlook != 1 and player.playerlook != 0:
        if player.playerlook == 2:
            player.snake = pygame.transform.rotate(player.snake,270)
        elif player.playerlook == 3:
            player.snake = pygame.transform.rotate(player.snake,90)
        player.playerlook = 0
    elif control[pygame.K_DOWN] and player.playerlook != 0 and player.playerlook != 1:
        if player.playerlook == 2:
            player.snake = pygame.transform.rotate(player.snake,90)
        elif player.playerlook == 3:
            player.snake = pygame.transform.rotate(player.snake,270)
        player.playerlook = 1
    elif control[pygame.K_LEFT] and player.playerlook != 3 and player.playerlook != 2:
        if player.playerlook == 1:
            player.snake = pygame.transform.rotate(player.snake,270)
        elif player.playerlook == 0:
            player.snake = pygame.transform.rotate(player.snake,90)
        player.playerlook = 2
    elif control[pygame.K_RIGHT] and player.playerlook != 2 and player.playerlook != 3:
        if player.playerlook == 1:
            player.snake = pygame.transform.rotate(player.snake,90)
        elif player.playerlook == 0:
            player.snake = pygame.transform.rotate(player.snake,270)
        player.playerlook = 3
    return player

def multiinputdir(player):
    control = pygame.key.get_pressed()
    if control[pygame.K_w] and player.playerlook != 1 and player.playerlook != 0:
        if player.playerlook == 2:
            player.snake = pygame.transform.rotate(player.snake,270)
        elif player.playerlook == 3:
            player.snake = pygame.transform.rotate(player.snake,90)
        player.playerlook = 0
    elif control[pygame.K_s] and player.playerlook != 0 and player.playerlook != 1:
        if player.playerlook == 2:
            player.snake = pygame.transform.rotate(player.snake,90)
        elif player.playerlook == 3:
            player.snake = pygame.transform.rotate(player.snake,270)
        player.playerlook = 1
    elif control[pygame.K_a] and player.playerlook != 3 and player.playerlook != 2:
        if player.playerlook == 1:
            player.snake = pygame.transform.rotate(player.snake,270)
        elif player.playerlook == 0:
            player.snake = pygame.transform.rotate(player.snake,90)
        player.playerlook = 2
    elif control[pygame.K_d] and player.playerlook != 2 and player.playerlook != 3:
        if player.playerlook == 1:
            player.snake = pygame.transform.rotate(player.snake,90)
        elif player.playerlook == 0:
            player.snake = pygame.transform.rotate(player.snake,270)
        player.playerlook = 3
    return player

def bodyfollow(player,screen,snakebody):
    for i in range(len(player.positions)-1,0,-1):
        playesposholder = []
        playesposholder.append(player.positions[i-1][0])
        playesposholder.append(player.positions[i-1][1])
        player.positions[i] = playesposholder
        screen.blit(snakebody,(player.positions[i][0],player.positions[i][1]))
    return player

def movement(player):
    if player.playerlook == 0:
        player.move(up=True,down=False,left=False,right=False)
    elif player.playerlook == 1:
        player.move(up=False,down=True,left=False,right=False)
    elif player.playerlook == 2:
        player.move(up=False,down=False,left=True,right=False)
    elif player.playerlook == 3:
        player.move(up=False,down=False,left=False,right=True) 
    return player