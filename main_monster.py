import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
monsterimage = ["images/rock01.png","images/rock02.png"]


def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad,clock,background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('PyShooting')
    background =pygame.image.load("images/background.png").convert_alpha()
    clock = pygame.time.Clock()


def runGame():
    global gamePad,clock,background

    monster = pygame.image.load(random.choice(monsterimage))
    monsterSize = monster.get_rect().size #monster 크기
    monsterWidth = monsterSize[0]
    monsterHeight = monsterSize[1]

    #monster초기 위치 설정
    monsterX = random.randrange(0,padWidth-monsterWidth)
    monsterY = 480
    monsterSpeed = 2


    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
        drawObject(background,0,0)
        clock.tick(60)

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

    pygame.quit()

initGame()
runGame()

