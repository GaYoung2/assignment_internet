import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init() 
pygame.display.set_caption("Simple PyGame Example")  #게임 화면 이름
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #게임스크린만들기


#커비 움직이기-----------------------------------------------------
pos_x = 0
pos_y = 400

clock = pygame.time.Clock() #시간설정
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_SPACE]:
        pos_y -= 10
        #잠시 시간이 필요
        #pos_y += 10

    if key_event[pygame.K_LEFT]:
        pos_x -= 1

    if key_event[pygame.K_RIGHT]:
        pos_x += 1

    if key_event[pygame.K_UP]:
        pos_y -= 1

    if key_event[pygame.K_DOWN]:
        pos_y += 1

    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20) #스크린에 흰색 크기가 20이고 x,y 좌표를가진것을 생성
    pygame.display.update()
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#몬스터 만들어서 랜덤으로 배치하기


