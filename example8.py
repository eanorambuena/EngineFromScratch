from engine import *

screen = Screen(200, 200)

for t in range(0, 100, 10):
    screen.fill_room()
    screen.triangle([-30, t], [0, -40 + t], [0, t], color = [255 - 2 * t, t, 255])
    screen.print_room()
