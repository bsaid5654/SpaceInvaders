from getaliens import *
from display_game import *
from getmissiles import *


game = Display_space()
stopped = False
gametime = 0
aliens1 = []
aliens = None
game.start()
missiles1 = []
missiles2 = []


def keycheck(keynow):
    if keynow == 'a':
        game.gameboard.resetposition(game.ss.x, game.ss.y)
        game.ss.moveleft()
        game.gameboard.fillposition(game.ss.x, game.ss.y, game.ss.pos)
    if keynow == 'd':
        game.gameboard.resetposition(game.ss.x, game.ss.y)
        game.ss.moveright()
        game.gameboard.fillposition(game.ss.x, game.ss.y, game.ss.pos)
    if keynow == 'Space':
        temp = Missile1(game.ss.x, game.ss.y)
        missiles1.append(temp)
        game.gameboard.fillposition(game.ss.x, game.ss.y-3, missiles1[0].pos)
    if keynow == 's':
        temp = Missile2(game.ss.x, game.ss.y)
        missiles2.append(temp)
        game.gameboard.fillposition(game.ss.x, game.ss.y-3, missiles2[0].pos)

while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                    keycheck('a')
            elif event.key == pygame.K_q:
                    stopped = True
            elif event.key == pygame.K_d:
                    keycheck('d')
            elif event.key == pygame.K_SPACE:
                    keycheck('Space')
            elif event.key == pygame.K_s:
                    keycheck('s')
            else:
                    pass

    for m1 in missiles1:
        m1.time = m1.time + 1
        if m1.time % 60 == 0:
            game.gameboard.resetposition(m1.x, m1.y)
            if aliens is not None:
                game.gameboard.fillposition(aliens.x, aliens.y, aliens.pos)
            m1.posupdate()
            checker = game.gameboard.checkposition(m1.x, m1.y)
            if checker == 0:
                game.gameboard.fillposition(m1.x, m1.y, m1.pos)
            elif checker == 1:
                game.updatescore()
                game.gameboard.resetposition(aliens.x, aliens.y)
                aliens = None
                missiles1.pop(missiles1.index(m1))
                continue
            elif checker == 2:
                for a1 in aliens1:
                    if a1.x == m1.x:
                        game.gameboard.resetposition(a1.x, a1.y)
                        aliens1.pop(aliens1.index(a1))
                        missiles1.pop(missiles1.index(m1))
                        game.updatescore()
                        continue
                continue
        if m1.y < 0:
            game.gameboard.resetposition(m1.x, m1.y)
            missiles1.pop(missiles1.index(m1))

    for m2 in missiles2:
        m2.time = m2.time+1
        if m2.time % 60 == 0:
            game.gameboard.resetposition(m2.x, m2.y)
            if aliens is not None:
                game.gameboard.fillposition(aliens.x, aliens.y, aliens.pos)
            m2.posupdate()
            checker = game.gameboard.checkposition(m2.x, m2.y)
            checker1 = game.gameboard.checkposition(m2.x, m2.y-3)
            if checker1 == 1:
                game.gameboard.resetposition(aliens.x, aliens.y)
                temp_alien = Alien1(aliens.x, aliens.y)
                aliens1.append(temp_alien)
                aliens = None
                missiles2.pop(missiles2.index(m2))
                continue
            elif checker1 == 2:
                for a1 in aliens1:
                    if a1.x == m2.x:
                        game.gameboard.resetposition(a1.x, a1.y)
                        aliens1.pop(aliens1.index(a1))
                        missiles2.pop(missiles2.index(m2))
                        game.updatescore()
                        continue
                continue
            if checker == 0:
                game.gameboard.fillposition(m2.x, m2.y, m2.pos)
            elif checker == 1:
                game.gameboard.resetposition(aliens.x, aliens.y)
                temp_alien = Alien1(aliens.x, aliens.y)
                aliens1.append(temp_alien)
                aliens = None
                missiles2.pop(missiles2.index(m2))
                continue
            elif checker == 2:
                for a1 in aliens1:
                    if a1.x == m2.x:
                        game.gameboard.resetposition(a1.x, a1.y)
                        aliens1.pop(aliens1.index(a1))
                        missiles2.pop(missiles2.index(m2))
                        game.updatescore()
                        continue
                continue
        if m2.y < 0:
            game.gameboard.resetposition(m2.x, m2.y)
            missiles2.pop(missiles2.index(m2))

    if gametime % 600 == 0:
        aliens = Alien()
        game.gameboard.fillposition(aliens.x, aliens.y, aliens.pos)

    if aliens is not None:
        if aliens.time == 480:
            game.gameboard.resetposition(aliens.x, aliens.y)
        aliens.time += 1

    if aliens1 is not None:
        for a1 in aliens1:
            a1.time += 1
            game.gameboard.fillposition(a1.x, a1.y, a1.pos)
            if a1.time == 300:
                game.gameboard.resetposition(a1.x, a1.y)
                aliens1.pop(aliens1.index(a1))

    gametime += 1
    game.gameboard.fillposition(game.ss.x, game.ss.y, game.ss.pos)
    game.setup()
    game.drawboard()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
