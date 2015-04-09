from math import sqrt

################################################################################
# vectors
# 

def vector(x, y, z):
    return (x, y, z)
def pos(x, y, z):
    return vector(x, y, z)
    
def vector_add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def vector_sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vector_scale(v, s):
    return list(map(lambda x: x * s, v))
    
def a_minus_bk(a, b, k):
    return [a[0] - b[0]*k, a[1] - b[1]*k, a[2] - b[2]*k]

def vector_normalize(v):
    magnitude = sqrt(dot_product(v, v))
    return list(map(lambda x: x / magnitude, v))

    
################################################################################
# spheres
#
def make_sphere(radius, center, color, exponent, reflectiveness):
    return (radius, center, color, exponent, reflectiveness)

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

################################################################################
# lights
# 
def light(intensity, coord):
    return (intensity, coord)

def light_intensity(l):
    return l[0]

def light_coord(l):
    return l[1]

################################################################################
# color
#

def color(red, green, blue):
    return (red, green, blue)

################################################################################
# util
#

def wait():
    #return
    raw_input("Press enter to exit")


def show_return(a):
    print(a)
    return a    
