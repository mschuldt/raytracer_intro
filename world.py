from things import *

canvas_size = 500
pen_size = 5

camera = [0, 0, 5]
reflection_depth = 3

spheres = [make_sphere(1, pos(0, 1,  0), color(1, 0, 0), 16, 0.5),
           make_sphere(1, pos(1, -1, 0), color(0, 1, 0), 16, 0.5),
           make_sphere(1, pos(-1, -1, 0), color(0, 0, 1), 16, 0.5)]

lights = [light(0.8, pos(0.5, 0.5, 5))]

ambient_light = 0.1


################################################################################

canvas_half = int(canvas_size/2)
