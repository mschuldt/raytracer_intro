from things import *

canvas_size = 300
pen_size = 1
render_using_turtle = False

camera = [0, 0, 5]
reflection_depth = 3

spheres = [make_sphere(1, pos(0, 1,  0), color(1, 0, 0), 16, 0.5),
           make_sphere(1, pos(1, -1, 0), color(0, 1, 0), 64, 0.5),
           make_sphere(1, pos(-1, -1, 0), color(0, 0, 1), 128, 0.5),
           make_sphere(0.5, pos(-0.5, 0, 1.5), color(1, 0, 1), 128, 0.5),
           ]

lights = [light(0.4, pos(-2, 0.5, 3))
          #light(0.8, pos(2, 0.5, 3)),
]

ambient_light = 0.1


################################################################################

canvas_half = int(canvas_size/2)
