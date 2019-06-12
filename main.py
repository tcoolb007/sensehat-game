import sense_hat
from time import sleep

sense = sense_hat.SenseHat()

sense.set_rotation(180)

b = [0, 0, 255]
w = [255, 255, 255]
g = [0, 255, 0]
y = [255, 255, 0]
e = [0, 0, 0]

man_x = 1
man_y = 4
path = [[0,4],[1,4],[1,3],[2,3],[3,3],[4,3],[4,4],[5,4],[6,4],[7,4]]
pressed = sense_hat.ACTION_PRESSED

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
b,b,b,b,b,b,b,w,
b,w,w,w,b,b,b,e,
b,w,w,w,b,b,w,w,
b,b,b,b,b,b,w,e,
b,b,g,g,b,b,b,w,
g,g,g,g,g,g,g,e,
g,g,g,g,g,g,g,w,
g,g,g,g,g,g,g,e
]

win = [
e,e,e,e,e,e,e,e,
e,e,y,e,e,y,e,e,
e,e,y,e,e,y,e,e,
e,e,y,e,e,y,e,e,
e,e,e,e,e,e,e,e,
e,y,e,e,e,e,y,e,
e,e,y,y,y,y,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(go)
running = True

def whitelist(x,y):
    for e in range(len(path)):
        item = path[e]
        if item == [x,y]: 
            return True
    return False 

while running:
    for event in sense.stick.get_events():
        if event.action == pressed:
            if event.direction == sense_hat.DIRECTION_UP and man_y < 7 and whitelist(man_x, man_y + 1):
                man_y = man_y + 1
            if event.direction == sense_hat.DIRECTION_DOWN and man_y > 0 and whitelist(man_x, man_y - 1):
                man_y = man_y - 1
            if event.direction == sense_hat.DIRECTION_LEFT and man_x < 7 and whitelist(man_x + 1, man_y):
                man_x = man_x + 1
            if event.direction == sense_hat.DIRECTION_RIGHT and man_x > 0 and whitelist(man_x - 1, man_y):
                man_x = man_x - 1
            sense.set_pixels(bg)
            sense.set_pixel(man_x, man_y, [255, 125, 0])
#        if event.type == QUIT:
#            running = False
    if man_x == 7:
        sense.set_pixels(win)
        print("\nyou win")
        sleep(10)
        running = False

print("bye")
sense.clear()
