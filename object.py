import pygame


class ball_class:

    def __init__(self,ball_size):
        self.xspeed=5
        self.yspeed=5
        self.object=pygame.image.load("graphic/ball1.png")
        self.xaxis=50
        self.yaxis=200
        self.score=10
        self.x_padding=ball_size
        self.y_padding = ball_size
        self.objectrect=self.object.get_rect()
        self.objectrect.left=self.xaxis
        self.objectrect.top = self.yaxis

    def wallcrash(self,screen_size,ballsize):
        x=screen_size[0]
        y=screen_size[1]
        #x and y is fullscreen x,y
        if (self.xaxis+ballsize)>x:
            self.xspeed=-self.xspeed
            return 1
        #right crash
        elif self.xaxis<0:
            self.xspeed=-self.xspeed
            return 2
        #left crash
        elif (self.yaxis+ballsize)>y:
            self.yspeed=-self.yspeed
            return 3
        #bottom crash

        elif self.yaxis<0:
            self.yspeed=-self.yspeed
            return 4
        #top crash
        else:
            return 0

    def move(self):
        self.xaxis=self.xaxis+self.xspeed
        self.yaxis = self.yaxis + self.yspeed
        self.objectrect.left=self.xaxis
        self.objectrect.top = self.yaxis

    def object_check(self,object):
        if object.check ==1:
            if self.objectrect.colliderect(object.objectrect):
                if (self.xaxis - object.xaxis) > 0 and (object.xaxis + object.x_padding) - (self.xaxis + self.x_padding) > 0:
                    self.yspeed=-self.yspeed
                if (self.yaxis-object.yaxis)>0 and (object.yaxis+object.y_padding)-(self.yaxis+self.y_padding)>0:
                    self.xspeed=-self.xspeed
                return 0
            else:
                return object.check
        else:
            return object.check
    def board_check(self,object):
        if self.objectrect.colliderect(object.objectrect):
            if (self.xaxis - object.xaxis) > 0 and (object.xaxis + object.x_padding) - (self.xaxis + self.x_padding) > 0:
                self.yspeed = -self.yspeed
            if (self.yaxis - object.yaxis) > 0 and (object.yaxis + object.y_padding) - (self.yaxis + self.y_padding) > 0:
                self.xspeed = -self.xspeed

class board:

    def __init__(self,board_size,screensize):
        self.xaxis=512
        self.yaxis=screensize[1]-board_size[1]
        self.speed=20
        self.x_padding=board_size[0]
        self.y_padding = board_size[1]
        self.object=pygame.image.load("graphic/board.png")
        self.objectrect=self.object.get_rect()
        self.objectrect.left=self.xaxis
        self.objectrect.top = self.yaxis
    def move_right(self):
        self.xaxis+=self.speed

    def move_left(self):
        self.xaxis-=self.speed

    def move(self,board_size,screen_size):

        x=screen_size[0]
        board_size_x=board_size[1]
        #screen_size is tuple
        key_input=pygame.key.get_pressed()

        if key_input[pygame.K_RIGHT]:
            self.move_right()
            if not(self.xaxis > 0 and (self.xaxis + self.x_padding) < x):
                self.move_left()
        if key_input[pygame.K_LEFT]:
            self.move_left()
            if not(self.xaxis > 0 and (self.xaxis + board_size_x) < x):
                self.move_right()
        self.objectrect.left=self.xaxis
        self.objectrect.top = self.yaxis

class block():
    def __init__(self,x,y,block_size):
        self.xaxis=x
        self.yaxis=y
        self.check=1
        self.x_padding=block_size[0]
        self.y_padding = block_size[1]
        #check mean boolean 0, 1 for touching check
        self.object=pygame.image.load("graphic/block.png")
        self.objectrect=self.object.get_rect()
        self.objectrect.left=self.xaxis
        self.objectrect.top = self.yaxis