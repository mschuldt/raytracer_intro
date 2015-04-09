#!/usr/bin/env python

from __future__ import division #for python 2
import turtle
from sys import argv

def usage_and_exit():
    print("Usage: python {basic, shadows, illum, raytracer}")
    exit(0)

if len(argv) != 2:
    usage_and_exit()
if argv[1] == "basic":
    from basic_raycasting import *
elif argv[1] == "shadows":
    from shadows_raycasting import *
elif argv[1] == "illum":
    from illuminated_raycasting import *
elif argv[1] == "raytracer":
    from basic_raytracer import *
else:
    usage_and_exit()

def render_with_turtle():
    turtle.pensize(pen_size)
    turtle.speed(0)
    turtle.shape("turtle")
    for y in range(-canvas_half, canvas_half, pen_size):
        turtle.penup()
        turtle.setpos(-canvas_half, y)
        turtle.pendown()
        for x in range(-canvas_half, canvas_half, pen_size):
            turtle.pencolor(pixel_color(x, y))
            turtle.forward(pen_size)
    wait()


def render_image(filename="output.png"):
    import png
    data = []
    for y in range(-canvas_half, canvas_half, pen_size):
        row = []
        for x in range(-canvas_half, canvas_half, pen_size):
            row.extend(list(map(lambda x: int(x*255) if x <= 1 else 255, pixel_color(x,y)*pen_size)))
        data.extend([row for _ in range(pen_size)])
        print ("{}%".format(((y + canvas_half)/canvas_size)*100))
    img = png.from_array(list(reversed(data)), 'RGB')
    img.save(filename)
    turtle.bgpic(filename)
    wait()

def pixel_color(x, y):
    direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
    return trace_ray(camera, direction)

if render_using_turtle:
    render_with_turtle()
else:
    render_image()
