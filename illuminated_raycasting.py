import turtle
from math import sqrt

turtle.speed(0)
turtle.shape("turtle")

canvas_size = 200
canvas_half = int(canvas_size/2)
pen_size = 5
camera = [0, 0, 5]

spheres = [[1, [0, 1,  0], [1, 0, 0], 16, 2],
           [1, [1, -1, 0], [0, 1, 0], 16, 2],
           [1, [-1, -1, 0], [0, 0, 1], 16, 2]]

lights = [(1, [0.5, 0.5, -5])]

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



def calc_specular(l, v, normal, p):
    reflected = calc_reflected(l, normal)
    return pow(max(0.0, dot_product(reflected, v)), p)

def calc_diffuse(l, normal):
    return max(0.0, dot_product(l, normal))


def calc_reflected(v, n):
    """ -v + 2 * dot(n, v) * n """
    dot_times_two = 2 * dot_product(v, n)
    return vector_sub(vector_scale(n, dot_times_two), v)

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vecotr_add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def vector_sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def vector_scale(v, s):
    return list(map(lambda x: x * s, v))

def vector_normalize(v):
    magnitude = sqrt(dot_product(v, v))
    return list(map(lambda x: x / magnitude, v))


def get_illumination(sphere, distance, v):
    surface = vector_scale(v, distance)
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
    return (closest, distance)


def trace_ray(direction):
    intersection = get_closest_intersection(camera, direction, 0, 100000)
    sphere = intersection[0]
    if sphere:
        color = sphere_color(sphere)
        illum = get_illumination(sphere, intersection[1], direction)
        return tuple(map(lambda channel: min(1.0, channel * illum), color))
    return (0, 0, 0)

turtle.pensize(pen_size)
turtle.speed(0)

for y in range(-canvas_half, canvas_half, pen_size):
    turtle.penup()
    turtle.setpos(-canvas_half, y)
    turtle.pendown()
    for x in range(-canvas_half, canvas_half, pen_size):
        v = vector_normalize([x/canvas_size, y/canvas_size, -1])
        color = trace_ray(v)
        turtle.pencolor(color)
        turtle.forward(pen_size)


### debugging

def show_return(a):
    print(a)
    return a

#wait
x = input()
