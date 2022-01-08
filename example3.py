from engine import *

screen = Screen()

from math import sin

screen.draw_axes()
screen.plot(sin, 0, 0, red)
screen.plot(sin, 0, 0, green, 40)

screen.print_room()
