# Lab 2
# 19 October 2020
# Created by YongHua
# Python version 3.8

import math

def box_volume(a, b, c):
    return a * b * c


print(box_volume(1, 1, 1))
print(box_volume(1, 2, 3.5))
print(box_volume(1, 1, 0))

def fall_time(h):
    return math.sqrt(2 * h / 9.81)

print(fall_time(10))
print(fall_time(1))

def interval_point(a, b, x):
    return (b - a) * x + a


print(interval_point(100, 200, 0.5))
print(interval_point(100, 200, 0.2))

def impact_velocity(h):
    return 2 * 9.81 * h


def degree(x):
    return x / math.pi * 180


print(degree(math.pi))

def seconds2days(n):
    return n / 86400


print(seconds2days(43200))

def box_surface(a, b, c):
    return 2*a*b + 2*b*c + 2*c*a


print(box_surface(1, 1, 1))
print(box_surface(2, 2, 0))

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))
