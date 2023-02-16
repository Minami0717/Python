import pygame
import random
import sys
import time

class Missile:
    missileX,missileY = None,None
    missile = pygame.image.load('missile.png')

    def shout():
        missileX = shipX + shipSize[0] / 2
        missileY = shipY

def paintEntity(entity,x,y):
    monitor.blit(entity,(int(x),int(y)))

def writeGameOver():
    myfont = pygame.font.Font('NanumGothic.ttf',40)
    txt = myfont.render(u'GAMEOVER', True, (255-r,255-g,255-b))
    monitor.blit(txt,(swidth/2-180,sheight/2-50))
    pygame.display.update()
    time.sleep(1)
    playGame()

def writeScore(score):
    myfont = pygame.font.Font('NanumGothic.ttf',20)
    txt = myfont.render(u'파괴한 우주괴물 수 : ' + str(score), True, (255-r,255-g,255-b))
    monitor.blit(txt,(10,sheight - 40))

def playGame():
    global monitor,ship,monster,missile

    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)

    shipX = swidth / 2
    shipY = sheight * 0.8
    dx,dy = 0,0

    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size
    monsterX = random.randrange(0,int(swidth))
    monsterY = 0
    monsterSpeed = random.randrange(5,10)
    sign = 1

    fireCount = 0

    while True:
        (pygame.time.Clock()).tick(100)
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT:dx = -10
                elif e.key == pygame.K_RIGHT:dx = +10
                elif e.key == pygame.K_UP:dy = -10
                elif e.key == pygame.K_DOWN:dy = +10
                elif e.key == pygame.K_SPACE:
                    m1 = Missile()
                    m1.shout()

            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT\
                   or e.key == pygame.K_UP or e.key == pygame.K_DOWN:dx,dy = 0,0

        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
            and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]):

            shipX += dx
            shipY += dy
        paintEntity(ship,shipX,shipY)

        monsterY += monsterSpeed
        if (monsterX >= int(swidth) or monsterX < 0):
            sign *= -1
        monsterX += (monsterSpeed * sign)
        
        if monsterY > sheight:
            monsterX = random.randrange(0,int(swidth))
            monsterY = 0
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(5,10)
            fireCount -=1

        paintEntity(monster,monsterX,monsterY)

        m1 = Missile()

        if m1.missileX != None:
            m1.missileY -= 10
            if m1.missileY < 0:
                m1.missileX,m1.missileY = None,None
                
        if m1.missileX != None:
            paintEntity(m1.missile,m1.missileX,m1.missileY)

            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
               (monsterY < missileY and missileY < monsterY + monsterSize[1]):
                fireCount += 1

                ship = pygame.image.load(random.choice(shipImage))

                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = random.randrange(0,int(swidth))
                monsterY = 0
                monsterSpeed = random.randrange(5,10)

                missileX,missileY = None,None

        mx1 = monsterX
        my1 = monsterY
        mx2 = monsterX + monsterSize[0]
        my2 = monsterY + monsterSize[1]
        sx1 = shipX
        sy1 = shipY
        sx2 = shipX + shipSize[0]
        sy2 = shipY + shipSize[1]

        meet = False

        if (sx1 < mx1 and mx1 < sx2) and (sy1 < my1 and my1 < sy2):
            meet = True
        elif (sx1 < mx2 and mx2 < sx2) and (sy1 < my2 and my2 < sy2):
            meet = True
        elif (sx1 < mx1 and mx1 < sx2) and (sy1 < my2 and my2 < sy2):
            meet = True
        elif (sx1 < mx2 and mx2 < sx2) and (sy1 < my1 and my1 < sy2):
            meet = True

        if (mx1 < sx1 and sx1 < mx2) and (my1 < sy1 and sy1 < my2):
            meet = True
        elif (mx1 < sx2 and sx2 < mx2) and (my1 < sy2 and sy2 < my2):
            meet = True
        elif (mx1 < sx1 and sx1 < mx2) and (my1 < sy2 and sy2 < my2):
            meet = True
        elif (mx1 < sx2 and sx2 < mx2) and (my1 < sy1 and sy1 < my2):
            meet = True

        if meet == True:
            writeGameOver()
                
        writeScore(fireCount)
        pygame.display.update()

r,g,b = [0] * 3
swidth,sheight = 1800,900
monitor = None
ship,shipSize = None,0

monsterImage = ['monster01.png','monster02.png','monster03.png','monster04.png',\
                'monster05.png','monster06.png','monster07.png','monster08.png',\
                'monster09.png','monster10.png']
monster = None


shipImage = ['ship01.png','ship02.png','ship03.png','ship04.png']

pygame.init()
monitor = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship =pygame.image.load('ship02.png')
shipSize = ship.get_rect().size


playGame()
