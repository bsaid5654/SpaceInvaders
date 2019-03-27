class Missile1:
    def __init__(self, a, b):
        self.pos = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.x = a
        self.y = b - 3
        self.speed = 1
        self.time = 1

    def posupdate(self):
        self.y = self.y - 3


class Missile2:
    def __init__(self, a, b):
        self.pos = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]
        self.x = a
        self.y = b - 3
        self.speed = 2
        self.time = 1

    def posupdate(self):
        self.y = self.y - 6
