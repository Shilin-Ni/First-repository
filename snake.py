class Point:
    row=0
    col=0
    def __init__(self,row,col):
        self.row=row
        self.col = col
    def copy(self,):
        return Point(row=self.row,col=self.col)




import pygame
import random
from pygame.locals import *

pygame.init()
w = 800
h = 600

ROW = 30
COL = 40

size = (w,h)
window = pygame.display.set_mode(size)#设置窗口
pygame.display.set_caption("贪吃蛇")#设置窗口名称

font_color = (255, 0, 0)
font=pygame.font.SysFont('SimHei',16)
surface1 = font.render(u'分数：0', True, (255, 0, 0))
textrect=surface1.get_rect()
window.blit(surface1,textrect)
pygame.draw.rect(window,font_color,(0,0,10,10))


def rect(point,color):#画形状
    cell_width=w/COL
    cell_height=h/ROW
    left=point.col* cell_width
    top=point.row* cell_height
    pygame.draw.rect(window,color,(left,top,cell_width,cell_height))

head=Point(row=int(ROW/2),col=int(COL/2))
head_color=(255,255,255)

snakes=[
    Point(row=head.row,col=head.col+1),
    Point(row=head.row, col=head.col + 2),
    Point(row=head.row,col=head.col+3)
]


def gen_food():
    while 1:
        pos=Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
        is_cell=False

        if pos.row==head.row and pos.col==head.col:
            is_cell=True
        for snake in snakes:
            if snake.row==pos.row and snake.col==pos.col:
                is_cell=True
                break
        if not is_cell:
            break
    return pos


 #定义坐标

food=gen_food()
food_color=(255,255,0)

bg_color = (255,255,255)
snake_color=(200,200,200)


snakes=[
    Point(row=head.row,col=head.col+1),
    Point(row=head.row, col=head.col + 1),
    Point(row=head.row,col=head.col+3)
]
#默认移动方向
direct='up'




quit = False
clock=pygame.time.Clock()
#游戏循环
while not quit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit=True
        elif event.type==pygame.KEYDOWN:
            if event.key==273 or event.key==119:
                if direct=='left' or direct=='right':
                    direct='up'
            elif event.key==274or event.key==115:
                if direct == 'left' or direct == 'right':
                    direct='down'
            elif event.key==276or event.key==97:
                if direct == 'up' or direct == 'down':
                    direct='left'
            elif event.key==275or event.key==100:
                if direct == 'up' or direct == 'down':
                    direct='right'
    #吃东西
    eat = (head.row==food.row and head.col==food.col)

    #处理身子
    #1.把原来的头插入到身体的头
    snakes.insert(0,head.copy())
    #2.把尾巴去掉
    if not eat:
        snakes.pop()
    if eat:
        food = gen_food()





    if direct=='left':
        head.col-=1
    elif direct=='right':
        head.col+=1
    elif direct=='up':
        head.row-=1
    elif direct=='down':
        head.row+=1


    #检测
    #1.撞墙
    #2.撞自己
    dead = False
    if head.col<0 or head.row<0 or head.row>ROW or head.col>COL:
        dead = True

    for snake in snakes:
        if head.col==snake.col and head.row==snake.row:
            dead = True
            break
    if dead:

        quit=True





#渲染
    pygame.draw.rect(window,bg_color,(0,0,w,h))
    #蛇头
    #食物
    for snake in snakes:
        rect(snake,snake_color)
    rect(food,food_color)
    rect(head,head_color)
    #设置帧频
    pygame.display.flip()
    clock.tick(10)
