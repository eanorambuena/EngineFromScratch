from engine import *

screen = Screen(200, 200)

screen.triangle([30, 0], [0, 40])
screen.print_room()
screen.triangle([30, 0], [0, 40], color = violet, zoom = 2)

screen.print_room()
