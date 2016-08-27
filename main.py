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

manX = 1
manY = 4
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
sleep(1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP and manY < 7:
                manY = manY + 1
            if event.key == K_DOWN and manY > 0:
                manY = manY - 1
            if event.key == K_LEFT and manX < 7:
                manX = manX + 1
            if event.key == K_RIGHT and manX > 0:
                manX = manX - 1
        if event.type == QUIT:
            running = False
            print("bye")
        sense.set_pixels(bg)
        sense.set_pixel(manX, manY, [255, 125, 0])

