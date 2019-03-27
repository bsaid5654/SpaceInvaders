import random


class Alien:
    def __init__(self):
        self.pos = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        self.x = random.randint(0, 7)
        self.y = random.randint(0, 1)
        self.x = self.x*3
        self.y = self.y*3
        self.time = 0


class Alien1:
    def __init__(self, a, b):
        self.pos = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]
        self.x = a
        self.y = b
        self.time = 0
