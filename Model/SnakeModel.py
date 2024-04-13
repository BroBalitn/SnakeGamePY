class Snake():
    def __init__(self, positions, snake, playerlook):
        self.positions = positions
        self.snake = snake
        self.playerlook = playerlook
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.positions[0][0] += 20
        if left:
            self.positions[0][0] -= 20
        if down:
            self.positions[0][1] += 20
        if up:
            self.positions[0][1] -= 20