import random

def applegen(player,player2=None):
    collide = True
    applepos = []
    appletop = 0
    appleright = 0
    while collide != False:
        appletop = random.randint(0,14) * 20
        appleright = random.randint(0,14) * 20
        for i in range(0,len(player.positions)):
            if player.positions[i][0] == appletop and player.positions[i][1] == appleright:
                collide = True
                break
            else:
                collide = False
        if player2 != None:
            for i in range(0,len(player2.positions)):
                if player2 != None and player2.positions[i][0] == appletop and player2.positions[i][1] == appleright:
                    collide = True
                    break
                else:
                    collide = False
    applepos.append(appletop)
    applepos.append(appleright)
    return applepos