from __future__ import division #for python 2
from math import sqrt
from world import *
from things import *

def calc_reflected(v, n):
    """ -v + 2 * dot(n, v) * n """
    dot_times_two = 2 * dot_product(v, n)
    return vector_sub(v, vector_scale(n, dot_times_two))

def calc_specular(l, v, normal, p):
    reflected = calc_reflected(l, normal)
    return pow(max(0.0, dot_product(reflected, v)), p)

def calc_diffuse(l, normal):
    return max(0.0, dot_product(l, normal))

def get_illumination(sphere, distance, v):
    surface = vector_add(vector_scale(v, distance), camera)
    normal = vector_normalize(vector_sub(surface, sphere_center(sphere)))
    p = sphere_exponent(sphere)

    coefficient = ambient_light
    for light in lights:
        light_vector = vector_normalize(vector_sub(light_coord(light), surface))
        curr_coeff = calc_diffuse(light_vector, normal) + calc_specular(light_vector, v, normal, p)
        coefficient += light_intensity(light) * curr_coeff

    return coefficient

def get_closest_intersection(source, direction, t_min, t_max):
    closest = None
    distance = t_max + 1
    for sphere in spheres:
        radius = sphere_radius(sphere)
        pos = sphere_center(sphere)
        v = vector_sub(source, pos)
        a = 2 * dot_product(direction, direction)
        b = - dot_product(v, direction)
        discr = b*b - (dot_product(v, v) - radius * radius)
        if discr > 0:
            discr = sqrt(discr)
            sol1 = (b + discr)
            if sol1 < distance and t_min < sol1 and t_max > sol1:
                distance = sol1
                closest = sphere
            sol2 = (b - discr)
            if sol2 < distance and t_min < sol2 and t_max > sol2:
                distance = sol2
                closest = sphere
    return (closest, distance)

def trace_ray(direction):
    intersection = get_closest_intersection(camera, direction, 0, 100000)
    sphere = intersection[0]
    if sphere:
        color = sphere_color(sphere)
        illum = get_illumination(sphere, intersection[1], direction)
        return tuple(map(lambda channel: min(1.0, channel * illum), color))
    return (0, 0, 0)

def pixel_color(x, y):
    direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
    return trace_ray(direction)
