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
    return sphere_color(sphere)
