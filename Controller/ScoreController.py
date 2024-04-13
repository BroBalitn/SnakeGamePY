def scoreblit(singlescores,screen,font2):
    with open("egyleaderboard.txt","rt") as f:
        for line in f:
            if line == "\n":
                continue
            data = []
            data = line.split('- ',1)[1]
            singlescores.append(data)
    for i in range(0,len(singlescores)):
        singlescores[i] = singlescores[i][:3]
    singlescores.sort(reverse=True)
    if len(singlescores) <= 5:
        for i in range(0,len(singlescores)):
            text = font2.render(singlescores[i],True, (255,255,255))
            screen.blit(text,(50,130 + i*30))
    else:
        for i in range(0,5):
            text = font2.render(singlescores[i],True, (255,255,255))
            screen.blit(text,(50,130 + i*30))
            
def multiscoreblit(multiscores, screen, font2):
    with open("tobbleaderboard.txt","rt") as f:
        for line in f:
            if line == "\n":
                continue
            data = []
            data = line.split('- ',1)[1]
            multiscores.append(data)
    for i in range(0,len(multiscores)):
        multiscores[i] = multiscores[i][:3]
    multiscores.sort(reverse=True)
    if len(multiscores) <= 5:
        for i in range(0,len(multiscores)):
            text = font2.render(multiscores[i],True, (255,255,255))
            screen.blit(text,(210,130 + i*30))
    else:
        for i in range(0,5):
            text = font2.render(multiscores[i],True, (255,255,255))
            screen.blit(text,(210,130 + i*30))