import pygame

from pygame.locals import *
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
pygame.init()
pygame.display.set_mode((640, 480))

sense.set_rotation(180)

b = [0, 0, 255]
w = [255, 255, 255]
g = [0, 255, 0]
e = [0, 0, 0]

man_x = 1
man_y = 4
blacklist = [[0,5],[1,5],[2,4],[3,4],[4,5],[5,5],[6,5],[7,5]]

go = [
e,e,e,e,e,e,e,e,
g,g,g,e,e,g,g,g,
g,e,e,e,e,g,e,g,
g,e,e,e,e,g,e,g,
g,e,g,g,e,g,e,g,
g,e,e,g,e,g,e,g,
g,g,g,g,e,g,g,g,
e,e,e,e,e,e,e,e
]

bg = [
b,b,b,b,b,b,b,b,
b,w,w,w,b,b,b,b,
b,w,w,w,b,b,w,w,
b,b,b,b,b,b,w,w,
b,b,g,g,b,b,b,b,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g
]

sense.clear()
sense.set_pixels(go)
running = True

def whitelist(x,y):
    scan = [x, y]
    for e in range(len(blacklist)):
        item = blacklist[e]
        if item == scan: 
            return False
    return True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP and man_y < 7 and whitelist(man_x, man_y + 1):
                man_y = man_y + 1
            if event.key == K_DOWN and man_y > 0 and whitelist(man_x, man_y - 1):
                man_y = man_y - 1
            if event.key == K_LEFT and man_x < 7 and whitelist(man_x + 1, man_y):
                man_x = man_x + 1
            if event.key == K_RIGHT and man_x > 0 and whitelist(man_x - 1, man_y):
                man_x = man_x - 1
            sense.set_pixels(bg)
            sense.set_pixel(man_x, man_y, [255, 125, 0])
        if event.type == QUIT:
            running = False
            print("bye")
            sense.clear()

