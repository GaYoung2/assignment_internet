import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
monsterimage = ["images/rock01.png","images/rock02.png"]
white = (255, 255, 255)

def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad,clock,background,curby
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('PyShooting')
    background =pygame.image.load("images/background.png").convert_alpha()
    curby = pygame.image.load("images/fighter.png").convert_alpha()
    clock = pygame.time.Clock()


def runGame():
    global gamePad,clock,background,curby

    curbySize = curby.get_rect().size
    curbyWidth = curbySize[0]
    curbyHeight = curbySize[1]
    curbyx = 0 #0.45 * padWidth
    curbyy = 480 #0.9 * padHeight
    curbyusex = 0
    curbyusey = 0
    

    monster = pygame.image.load(random.choice(monsterimage))
    monsterSize = monster.get_rect().size #monster 크기
    monsterWidth = monsterSize[0]
    monsterHeight = monsterSize[1]
    #monster초기 위치 설정
    monsterX = random.randrange(0,padWidth-monsterWidth)
    monsterY = 480
    monsterSpeed = 1

    onGame = False
    #key_event = pygame.key.get_pressed()
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
            key_event = pygame.key.get_pressed()

            if key_event[pygame.K_SPACE]:
                curbyusey -= 1
            #잠시 시간이 필요
            #pos_y += 10
            if key_event[pygame.K_LEFT]:
                curbyusex -= 5

            if key_event[pygame.K_RIGHT]:
                curbyusex += 5

            if key_event[pygame.K_UP]:
                curbyusey -= 5

            if key_event[pygame.K_DOWN]:
                curbyusey += 5
            #pygame.draw.circle(background, white, (pos_x, pos_y), 20)

        drawObject(background,0,0)
        curbyx +=curbyusex
        curbyy +=curbyusey

        if curbyx<0:
            curbyx = 0
        elif curbyx>padWidth-curbyWidth:
            curbyx = padWidth - curbyWidth
        drawObject(curby,curbyx,curbyy)
            #pygame.draw.circle(background, white, (pos_x, pos_y), 20)

        monsterX -=monsterSpeed
        if monsterX < 0: #몬스터가 없어지면 새로운 몬스터를 부른다.
            monster = pygame.image.load(random.choice(monsterimage))
            monsterSize = monster.get_rect().size
            monsmonsterWidth = monsterSize[0]
            monsterHeight = monsterSize[1]
            monsterX = random.randrange(0,padWidth-monsterWidth)
            monsterY = 400
        drawObject(monster,monsterX,monsterY)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

initGame()
runGame()

