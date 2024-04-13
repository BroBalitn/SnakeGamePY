def wallcollide(player):
    if player.positions[0][0] < 0 or player.positions[0][1] < 0:
        return True
    if player.positions[0][0] > 280 or player.positions[0][1] > 280:
        return True

def bodycollide(player):
    for i in range(1,len(player.positions)):
        if player.positions[0] == player.positions[i]:
            return True

def playercollide(player,player2):
    for i in range(0,len(player.positions)):
        for j in range(0,len(player2.positions)):
            if player.positions[i] == player2.positions[j]:
                return True