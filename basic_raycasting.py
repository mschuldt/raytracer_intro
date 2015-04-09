from __future__ import division #for python 2
import turtle
import png
from math import sqrt
from world import *
from things import *


def get_closest_sphere(source, direction, t_min, t_max):
    closest = None
    distance = t_max + 1
    for sphere in spheres:
        radius = sphere_radius(sphere)
        pos = sphere_center(sphere)
        v = vector_sub(source, pos)
        b = - dot_product(v, direction)
        discr = b*b - (dot_product(v, v) - radius * radius)
        if discr > 0:
            discr = sqrt(discr)
            sol1 = b - discr
            if sol1 < distance and t_min < sol1 and t_max > sol1:
                distance = sol1
                closest = sphere
            sol2 = b + discr
            if sol2 < distance and t_min < sol2 and t_max > sol2:
                distance = sol2
                closest = sphere
    return closest, distance


def trace_ray(source, direction):
    sphere, distance = get_closest_sphere(camera, direction, 0.001, 100000)
    if not sphere:
        return [0, 0, 0]
    x = a_minus_bk(source, direction, distance)
    n = list(map(abs, vector_sub(x, sphere_center(sphere))))
    m = max(n)
    return list(map(lambda x: x/m, n))

################################################################################

def render_with_turtle():
    turtle.pensize(pen_size)
    turtle.speed(0)
    turtle.shape("turtle")

    for y in range(-canvas_half, canvas_half, pen_size):
        turtle.penup()
        turtle.setpos(-canvas_half, y)
        turtle.pendown()
        for x in range(-canvas_half, canvas_half, pen_size):
            color = trace_ray(camera, vector_normalize([x/canvas_size, y/canvas_size, -1]))
            turtle.pencolor(color)
            turtle.forward(pen_size)
    wait()


def render_image(filename="output.png"):
    data = []
    for y in range(-canvas_half, canvas_half, pen_size):
        row = []
        for x in range(-canvas_half, canvas_half, pen_size):
            direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
            color = list(map(lambda c: min(1.0, c), trace_ray(direction)))
            row.extend(map(lambda x: int(x*255), color*pen_size))
        data.extend([row for _ in range(pen_size)])
        print ("{}%".format(((y + canvas_half)/canvas_size)*100))
    img = png.from_array(list(reversed(data)), 'RGB')
    img.save(filename)
    turtle.bgpic(filename)
    wait()

# render_with_turtle()
render_image()
