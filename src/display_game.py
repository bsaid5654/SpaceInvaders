import pygame
from getspaceship import *
from getboard import *

pygame.init()
size = [700, 520]
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 0, 255)
gd = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()


class Display_space(Board, Spaceship):
    def __init__(self):
        self.score = 0
        self.gameboard = Board()
        self.ss = Spaceship()
        self.gamescore = "Score: 0"

    def drawboard(self):
        for i in range(0, 24):
            for j in range(0, 24):
                if self.gameboard.boardpos[i][j] == 1:
                    pygame.draw.rect(gd, black, [i*20+22, j*20+22, 15, 15])

    def display_text(self, txt, color, size, x, y):
        msg = pygame.font.SysFont(None, size)
        fin = msg.render(txt, True, color)
        gd.blit(fin, [x, y])

    def setup(self):
        gd.fill(black)
        pygame.draw.rect(gd, white, [10, 10, 500, 500])
        pygame.draw.rect(gd, white, [530, 80, 150, 150])
        pygame.draw.rect(gd, white, [530, 280, 150, 150])
        self.display_text("Controls:", red, 24, 535, 82)
        self.display_text("Left:        a", red, 24, 535, 107)
        self.display_text("Right:     d", red, 24, 535, 132)
        self.display_text("Shoot1: Space", red, 24, 535, 157)
        self.display_text("Shoot2: s", red, 24, 535, 182)
        self.display_text("Quit:       q", red, 24, 535, 207)
        self.display_text(self.gamescore, green, 40, 540, 335)

    def updatescore(self):
        self.score += 1
        self.gamescore = "Score: " + str(self.score)

    def start(self):
        self.setup()
        self.gameboard.fillposition(self.ss.x, self.ss.y, self.ss.pos)
