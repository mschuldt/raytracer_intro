from __future__ import division #for python 2
import turtle
import png

canvas_size = 200
canvas_half = int(canvas_size/2)
pen_size = 1
camera = [0, 0, -5]

spheres = [[1, [0, 1,  0]],
           [1.2, [1, -1, 0]],
           [1, [-1, -1, 0]]]

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vector_sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def a_minus_bk(a, b, k):
    return [a[0] - b[0]*k, a[1] - b[1]*k, a[2] - b[2]*k]

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

def render_with_turtle():
    turtle.pensize(pen_size)
    turtle.speed(0)
    for y in range(-canvas_half, canvas_half, pen_size):
        turtle.penup()
        turtle.setpos(-canvas_half, y)
        turtle.pendown()
        for x in range(-canvas_half, canvas_half, pen_size):
            color = trace_ray([x/canvas_size, y/canvas_size, 1])
            turtle.pencolor(color)
            turtle.forward(pen_size)
    wait()

def render_image(filename="output.png"):
    data = []
    for y in range(-canvas_half, canvas_half, pen_size):
        row = []
        for x in range(-canvas_half, canvas_half, pen_size):
            color = trace_ray([x/canvas_size, y/canvas_size, 1])
            row.extend(map(lambda x: int(x*255), color))
        data.append(row)
        print ("{}%".format(((y + canvas_half)/canvas_size)*100))
    img = png.from_array(data, 'RGB')
    img.save(filename)
    turtle.bgpic(filename)
    wait()

def wait(): raw_input()

#render_with_turtle()
render_image()
