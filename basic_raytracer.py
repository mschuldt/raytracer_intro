from __future__ import division #for python 2
import png
import turtle
from math import sqrt

canvas_size = 400
canvas_half = int(canvas_size/2)
pen_size = 5
camera = [0, 0, 5]
reflection_depth = 3

spheres = [[1, [0, 1,  0], [1, 0, 0], 16, 0.5],
           [1, [1, -1, 0], [0, 1, 0], 16, 0.5],
           [1, [-1, -1, 0], [0, 0, 1], 16, 0.5]]

lights = [(0.8, [0.5, 0.5, 5])]

ambient_light = 0.1


def light_intensity(l):
    return l[0]

def light_coord(l):
    return l[1]


def sphere_radius(s):
    return s[0]

def sphere_center(s):
    return s[1]

def sphere_color(s):
    return s[2]

def sphere_exponent(s):
    return s[3]

def sphere_reflectiveness(s):
    return s[4]

def calc_reflected(v, n):
    """ v - 2 * dot(n, v) * n """
    dot_times_two = 2 * dot_product(v, n)
    return vector_sub(v, vector_scale(n, dot_times_two))

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vector_add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def vector_sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def vector_scale(v, s):
    return list(map(lambda x: x * s, v))

def vector_normalize(v):
    magnitude = sqrt(dot_product(v, v))
    return list(map(lambda x: x / magnitude, v))

#### ACTUAL LOGIC ####

def calc_specular(l, v, normal, p):
    reflected = calc_reflected(l, normal)
    return pow(max(0.0, dot_product(reflected, v)), p)


def calc_diffuse(l, normal):
    return max(0.0, dot_product(l, normal))


def get_illumination(sphere, surface, v, normal):
    p = sphere_exponent(sphere)

    coefficient = ambient_light
    for light in lights:
        light_vector = vector_normalize(vector_sub(light_coord(light), surface))

        ## SHADOWS
        closest = get_closest_intersection(surface, light_vector, 0.001, 100000)
        if closest[0]:
            continue

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
    return closest, distance


def trace_ray(source, direction, depth):
    if depth == 0:
        return [0, 0, 0]

    intersection = get_closest_intersection(source, direction, 0.01, 100000)
    sphere = intersection[0]
    distance = intersection[1]
    if sphere:
        refl = sphere_reflectiveness(sphere)
        surface = vector_add(vector_scale(direction, distance), source)
        normal = vector_normalize(vector_sub(surface, sphere_center(sphere)))

        # get current sphere color
        curr_illum = get_illumination(sphere, surface, direction, normal)
        curr_color = vector_scale(sphere_color(sphere), curr_illum * (1 - refl))

        # get reflected color
        r = calc_reflected(direction, normal)
        reflection = vector_scale(trace_ray(surface, r, depth - 1), refl)

        return vector_add(curr_color, reflection)
    return [0, 0, 0]


def render_with_turtle():
    turtle.pensize(pen_size)
    turtle.speed(0)
    turtle.shape("turtle")

    for y in range(-canvas_half, canvas_half, pen_size):
        turtle.penup()
        turtle.setpos(-canvas_half, y)
        turtle.pendown()
        for x in range(-canvas_half, canvas_half, pen_size):
            direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
            color = list(map(lambda c: min(1.0, c), trace_ray(camera, direction, reflection_depth)))
            turtle.pencolor(color)
            turtle.forward(pen_size)
    wait()

def render_image(filename="output.png"):
    data = []
    for y in range(-canvas_half, canvas_half, pen_size):
        row = []
        for x in range(-canvas_half, canvas_half, pen_size):
            direction = vector_normalize([x/canvas_size, y/canvas_size, -1])
            color = list(map(lambda c: min(1.0, c), trace_ray(camera, direction, reflection_depth)))
            row.extend(map(lambda x: int(x*255), color))
        data.append(row)
        print ("{}%".format(((y + canvas_half)/canvas_size)*100))
    img = png.from_array(data, 'RGB')
    img.save(filename)
    turtle.bgpic(filename)
    wait()

def wait(): raw_input()

### debugging

def show_return(a):
    print(a)
    return a

render_image();

#wait
x = input()