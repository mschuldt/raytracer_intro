from __future__ import division #for python 2
import turtle

from basic_raycasting import *
#from shadows_raycasting import *
#from illuminated_raycasting import *
#from basic_raytracer import *


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

#render_with_turtle()
render_image()
