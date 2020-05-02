import pygame
import sys
import random
from time import sleep
from pygame.locals import *
pygame.font.init()

padWidth = 500
padHeight = 500
monsterimage = ["pyshooting/rock01.png","pyshooting/rock02.png"]
GRAY =(100,100,100)
background_width = 500

def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))

def back(background,x,y):
    global gamePad
    gamePad.blit(background,(x,y))

def initGame():
    global gamePad,clock,background,curby,background2
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('PyShooting')
    background =pygame.image.load("pyshooting/karbybackground2.png").convert_alpha()
    background2 = background.copy()
    curby = pygame.image.load("pyshooting/fighter.png").convert_alpha()
    clock = pygame.time.Clock()


def runGame():
    global gamePad,clock,background,curby,background2
    background_x = 0
    background2_x = background_width
    isJump = False
    jumpCount = 10

    curbySize = curby.get_rect().size
    curbyWidth = curbySize[0]
    curbyHeight = curbySize[1]
    curbyusex = 50
    curbyusey = 440
    vel = 5

    monster = pygame.image.load(random.choice(monsterimage))
    monsterSize = monster.get_rect().size #monster 크기
    monsterWidth = monsterSize[0]
    monsterHeight = monsterSize[1]
    #monster초기 위치 설정
    monsterX = 440
    monsterY = 440
    monsterSpeed = 6

    crashed = False
    #key_event = pygame.key.get_pressed()
    while not crashed:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        key_event = pygame.key.get_pressed()
            #if event.type == pygame.KEYDOWN:
        if key_event[pygame.K_LEFT] and curbyusex >vel:
            curbyusex -= vel
        if key_event[pygame.K_RIGHT] and curbyusex < 500 - curbyWidth - vel:
            curbyusex += vel
        if not (isJump):
            if key_event[pygame.K_UP] and curbyusey > vel:
                curbyusey -= vel
            if key_event[pygame.K_DOWN] and curbyusey < 500 - curbyHeight - vel:
                curbyusey += vel
            if key_event[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >=-10:
                neg = 1
                if jumpCount <0:
                    neg = -1
                curbyusey -=(jumpCount**2)*0.5*neg
                jumpCount -=1
            else:
                isJump = False
                jumpCount = 10
        drawObject(background,0,0)
           

        background2_x-=2
        background_x-=2
        if background_x==-background_width:
            background_x=background_width
        if background2_x==-background_width:
            background2_x=background_width
        back(background,background_x,0)
        back(background2,background2_x,0)
        drawObject(curby,curbyusex,curbyusey)

        monsterX -=monsterSpeed
        if monsterX < 50: #몬스터가 없어지면 새로운 몬스터를 부른다.
            monster = pygame.image.load(random.choice(monsterimage))
            monsterSize = monster.get_rect().size
            monsterWidth = monsterSize[0]
            monsterHeight = monsterSize[1]
            monsterX = 450
            monsterY = 450
        drawObject(monster,monsterX,monsterY)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

initGame()
runGame()
#pygame.font.get_fonts()