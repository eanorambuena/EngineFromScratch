from engine import *

screen = Screen()

screen.draw_axes()

camera = Camera3d(1, 1, 1, 2)

A = origin
B = [10, 0, 0]
C = [10, 10, 0]
D = [0, 10, 0]
E = [0, 0, 10]
F = [10, 0, 10]
G = [10, 10, 10]
H = [0, 10, 10]
cube = Body([
    Triangle(A, C, D, red),
    Triangle(A, B, C, green),
    Triangle(A, B, F)
])

cube.draw(camera, screen)

screen.print_room()