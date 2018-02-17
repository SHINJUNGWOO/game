import pygame,sys
from object import ball_class,board,block
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.display.set_caption("GAME")
screen_size=(1024,512)
screen = pygame.display.set_mode(screen_size)

fps=60
clock = pygame.time.Clock()

font=pygame.font.Font(None,32)
font1=pygame.font.Font(None,128)

ball_size = 8
ball_number=1
board_size=(128,32)
block_size=(128,32)
life=10
gamemode=0

ball=[]
ball.append(ball_class(ball_size))
board1=board(board_size)
array=[]

for y in range(3):
    temp_array = []
    for x in range(8):
        temp_array.append(block((x*block_size[0]),(y*block_size[1]),block_size))
    array.append(temp_array)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type ==KEYDOWN:
            if event.key==K_ESCAPE:
                sys.exit()
    screen.fill((255, 255, 255))
    for i in range(len(ball)):
        ball[i].move()
        wallcode=ball[i].wallcrash(screen_size,ball_size)

        ball[i].board_check(board1)
    board1.move(board_size,screen_size)

    if wallcode==3:
        life-=1
    if life==0:
        gamemode=1


    for y in range(3):
        for x in range(8):
            for i in range(len(ball)):
                array[y][x].check=ball[i].object_check(array[y][x])




    lifetext="life:"+str(life)
    text1 = font.render(lifetext, True, (0,0,0))
    text1Rect = text1.get_rect()
    text1Rect.top=5
    text1Rect.left=20


    scoretext="score:"+str(len(ball))
    text2 = font.render(scoretext, True, (0,0,0))
    text2Rect = text2.get_rect()
    text2Rect.top=35
    text2Rect.left=20

    gameover_text="GAMEOVER"
    text3 = font1.render(gameover_text, True, (0,0,0))
    text3Rect = text3.get_rect()
    text3Rect.top=128
    text3Rect.left=256

    if gamemode==0:
        for i in range(len(ball)):
            screen.blit(ball[i].object,ball[i].objectrect)
        left_ball_check=0
        for y in range(3):
            for x in range(8):
                if array[y][x].check==1:
                    left_ball_check+=1
                    screen.blit(array[y][x].object, array[y][x].objectrect)
        if left_ball_check<5:
            for y in range(3):
                for x in range(8):

                    array[y][x].check=1
            ball.append(ball_class(ball_size))

        screen.blit(text1,text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(board1.object,board1.objectrect)
    elif gamemode==1:
        text2Rect.top=300
        text2Rect.left = 470
        screen.blit(text3, text3Rect)
        screen.blit(text2, text2Rect)
    else:
        gamemode=0



    pygame.display.flip()
    clock.tick(fps)