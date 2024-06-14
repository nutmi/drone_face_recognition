import numpy as np


def calculate_fb(area, fbmin, fbmax):

    fbmin, fbmax = 60000, 70000
    if area > fbmin and area < fbmax:
        fb = 0
    elif area > fbmax:
        fb = -20
    elif area < fbmin and area != 0:
        fb = 20

    return fb

def calculate_heigh(distance_y):
    move_threshold = 20
    if abs(distance_y) > move_threshold:
        if distance_y < 0:
            heigh = 20
        else:
            heigh = -20
    
    return heigh

def calculate_yaw_speed(distance_x):

    propotional_gain = 0.1

    yaw_speed = distance_x * propotional_gain
    yaw_speed = int(np.clip(yaw_speed, -100, 100))

    return yaw_speed

def drone_calculation(distance_x, distance_y, area):

    lf = 0
    yaw_speed = calculate_yaw_speed(distance_x)
    heigh,fb = calculate_heigh(distance_y), calculate_fb(area)

    return lf, fb, heigh ,yaw_speed