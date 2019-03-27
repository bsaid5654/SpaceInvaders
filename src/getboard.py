class Board:
    def __init__(self):
        self.boardpos = [[0 for i in range(0, 24)] for j in range(0, 24)]

    def fillposition(self, a, b, arr):
        for i in range(a, a+3):
            for j in range(b, b+3):
                if arr[i-a][j-b] == 1:
                    self.boardpos[i][j] = 1
                else:
                    self.boardpos[i][j]

    def checkposition(self, x, y):
        if self.boardpos[x][y] == 1 and self.boardpos[x][y+2] == 1:
            if self.boardpos[x+1][y] == 1:
                return 2
            else:
                return 1
        return 0

    def resetposition(self, x, y):
        for i in range(x, x+3):
            for j in range(y, y+3):
                self.boardpos[i][j] = 0
