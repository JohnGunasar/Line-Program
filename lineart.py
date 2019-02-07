## DISTRUBTION OF THIS CODE IS ALLOWED AS LONG AS YOU DO NOT CLAIM IT AS YOUR OWN
## ORIGINAL CREATER OF PROGRAM: REDDIT USER 20gunasarj

import math
import pygame as pg
import random
pg.init()

cr = [[1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0]]
co = [[960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0]]
cy = [[480, 0], [960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270]]
cg = [[1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710]]
cb = [[1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080]]
ci = [[1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080], [960, 1080]]
cv = [[960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270], [0, 710], [480, 1080]]
clb = [[480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270], [0, 710]]
clg = [[0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0], [0, 270]]
cp = [[0, 270], [0, 710], [480, 1080], [960, 1080], [1440, 1080], [1920, 710], [1920, 270], [480, 0], [960, 0], [1440, 0]]

def increaseEach(arr,n1,n2):
    for i in range(len(arr)):
            arr[i][0] += n1//2
            arr[i][1] += n2//2
    return arr

red = 255,0,0 # 0 
orange = 255,165,0 # 1
yellow = 255,255,0 # 2
green = 0,255,0 # 3
blue = 0,0,255 # 4
indigo = 128,0,128 # 5
violet = 153,50,204 # 6
light_blue = 135,206,250 # 7
light_green = 34,139,34 # 8
pink = 255,192,203 # 9
white = (255,255,255)
black = (0,0,0)

def pi():
    display_width = 1920
    display_height = 1080
    screen = pg.display.set_mode((display_width,display_height))
    n = 0
    clock = pg.time.Clock()
    pC = random.randint(1,9)
    index = 9 - pC
    while n < 100:
        count = 0
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        range1 = random.randint(-50,0)
        range2 = random.randint(0,50)
        range3 = random.randint(-50,0)
        range4 = random.randint(0,50)
        
        n1 = random.randint(range1,range2)
        n2 = random.randint(range3,range4)
        w = random.randint(1,10)
        lim = random.randint(0,50)

        for x in range(0,lim):  # RED
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cr,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,red,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(cr,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,red,sc,ec,w)

        for x in range(0,lim):  # ORANGE
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(co,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,orange,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(co,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,orange,sc,ec,w)

        for x in range(0,lim):  # YELLOW
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cy,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,yellow,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(cy,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,yellow,sc,ec,w)

        for x in range(0,lim):  # GREEN
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cg,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,green,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(cg,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,green,sc,ec,w)

        for x in range(0,lim):  # BLUE
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cb,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,blue,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(cb,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,blue,sc,ec,w)

        for x in range(0,lim):  # INDIGO
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(ci,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,indigo,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(ci,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,indigo,sc,ec,w)

        for x in range(0,lim):  # VIOLET
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cv,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,violet,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(cv,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,violet,sc,ec,w)

        for x in range(0,lim):  # LIGHT BLUE
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(clb,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,light_blue,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(clb,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,light_blue,sc,ec,w)

        for x in range(0,lim):  # LIGHT GREEN
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(clg,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[index][1])
                    pg.draw.line(screen,light_green,sc,ec,w)
                if x % 2 == 1:
                    j = increaseEach(clg,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,light_green,sc,ec,w)

        for x in range(0,lim):  # PINK
            for y in range(0,pC):
                if x % 2 == 0:
                    j = increaseEach(cp,n1,n1)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,pink,sc,ec,w-1)
                if x % 2 == 1:
                    j = increaseEach(cp,n2,n2)
                    sc = (j[y][0],j[y][1])
                    ec = (j[y+index][0],j[y+index][1])
                    pg.draw.line(screen,pink,sc,ec,w-1)

        n += random.randint(1,99)
        pg.display.update()
        clock.tick(1000)

pi()
