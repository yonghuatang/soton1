# Lab 5 (Online Lab)
# 09 November 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import numpy as np

def count_vowels(s):
    """Returns the number of letters 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    in a given string s"""

    letters = "aeiouAEIOU"
    count = 0
    for letter in s:
        if letter in letters:
            count += 1
    return count


def vector_product3(a, b):
    """With inputs a=[ax, ay, az] and b=[bx, by, bz], the function returns a list
    which contains the vector product of 3d-vectors a and b"""

    v1 = np.array(a)
    v2 = np.array(b)
    return list(np.cross(a, b))


def seq_mult_scalar(a, s):
    """Takes a list of numbers a and a scalar s. For the input a=[a0, a1, a2,.., an]
    the function returns [s * a0, s * a1, s * a2, ..., s * an]"""

    return [s * i for i in a]


def powers(n, k):
    """Returns the list [1,n,n^2,n^3,...,n^k] where k is an integer"""

    return [n ** k for k in range(k+1)]


def traffic_light(load):
    """Takes a floating point number load.
    The function should return the string:

    "green" for values of load below 0.7
    "amber" for values of load equal to or greater than 0.7 but smaller than 0.9
    "red" for values of load equal to 0.9 or greater than 0.9"""

    if load < 0.7:
        return "green"
    elif 0.7 <= load < 0.9:
        return "amber"
    elif load >= 0.9:
        return "red"


def box_volume_UPS(a=13, b=11, c=2):
    """Returns the volume of a box with edge lengths a, b and c.
    Default values are a = 13 inches, b = 11 inches and c = 2 inches"""

    return a * b * c
