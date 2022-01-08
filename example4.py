from engine import *
from eggdriver import sleep

screen = Screen(200, 200)

c = [red, green, blue, white, pink, violet]

for i in range(len(c)):
    screen.draw_flower(i + 1, color = c[i])
    screen.print_room()
    sleep(1000)


