def bodygrow(bodygrow):
    if bodygrow.applepos[0] == bodygrow.player.positions[0][0] and bodygrow.applepos[1] == bodygrow.player.positions[0][1]:
        bodygrow.score += 1
        bodygrow.applespawn = True
        if bodygrow.player.positions[len(bodygrow.player.positions)-1][0] - 20 == bodygrow.player.positions[len(bodygrow.player.positions)-2][0]:
            newbody = []
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][0] + 20)
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][1])
            bodygrow.player.positions.append(newbody)
        elif bodygrow.player.positions[len(bodygrow.player.positions)-1][0] + 20 == bodygrow.player.positions[len(bodygrow.player.positions)-2][0]:
            newbody = []
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][0] - 20)
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][1])
            bodygrow.player.positions.append(newbody)
        elif bodygrow.player.positions[len(bodygrow.player.positions)-1][1] - 20 == bodygrow.player.positions[len(bodygrow.player.positions)-2][1]:
            newbody = []
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][0])
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][1] + 20)
            bodygrow.player.positions.append(newbody)
        elif bodygrow.player.positions[len(bodygrow.player.positions)-1][1] + 20 == bodygrow.player.positions[len(bodygrow.player.positions)-2][1]:
            newbody = []
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][0])
            newbody.append(bodygrow.player.positions[len(bodygrow.player.positions)-1][1] - 20)
            bodygrow.player.positions.append(newbody)
    return bodygrow