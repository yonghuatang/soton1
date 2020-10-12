# Lab 1
# 12 October 2020
# Created by YongHua
# Python version 3.9

import math

def average(a, b):
    return (a + b) * 0.5


print(average(10, 20))
print(average(10, 4))

def distance(a, b):
    if a > b:
        return a - b
    else:
        return b - a


print(distance(3, 4))
print(distance(3, 1))

def geometric_mean(a, b):
    return math.sqrt(a * b)


print(geometric_mean(2, 2))
print(geometric_mean(2, 8))
print(geometric_mean(2, 1))

def pyramid_volume(A, h):
    return (1/3) * A * h


print(pyramid_volume(1, 2))
