from engine import *

screen = Screen(200, 200)

screen.draw_axes()
screen.draw_triangle([30, 0], [0, 40])
screen.draw_line([30, 0], zoom = -1)

screen.print_room()

print(screen.is_point_inside_triangle([-1,1], [[30, 0], [0, 40], [0,0]]))