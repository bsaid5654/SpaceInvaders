class Spaceship:
    def __init__(self):
        self.pos=[[0,1,0],[1,1,1],[0,1,0]]
        self.x=0
        self.y=21
    def moveleft(self):
        if self.x>0:
            self.x=self.x-3
    def moveright(self):
        if self.x<21:
            self.x=self.x+3
