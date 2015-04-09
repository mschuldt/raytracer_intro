from __future__ import division #for python 2
import turtle
import png
from math import sqrt
from world import *
from things import *

def get_closest_sphere(source, direction, t_min, t_max):
    closest = None;
    distance = t_max + 1
    for sphere in spheres:
        radius = sphere[0]
        pos = sphere[1]
        v = vector_sub(source, pos)
        a = 2 * dot_product(direction, direction)
        b = -2 * dot_product(v, direction)
        discr = b*b - 2 * a * (dot_product(v, v) - radius * radius)
        if discr > 0:
            sol1 = (b - discr) / a
            if sol1 < distance and t_min < sol1 and t_max > sol1:
                distance = sol1
                closest = sphere
            sol2 = (b + discr) / a
            if sol2 < distance and t_min < sol2 and t_max > sol2:
                distance = sol2
                closest = sphere
    return closest, distance

def trace_ray(direction):
    s,d = get_closest_sphere(camera, direction, 0, 100000)
    if not s:
        return (0, 0, 0)
    x = a_minus_bk(camera, direction, -d)
    n = list(map(abs,vector_sub(x, s[1])))
    m = max(n)
    return tuple(map(lambda x: x/m, n))

def pixel_color(x, y):
    direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
    return trace_ray(direction)
