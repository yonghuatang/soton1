# Lab 3
# 26 October 2020
# Created by YongHua
# Python version 3.8

import math

def signum(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return 0


print(signum(2012))

def min_max(xs):
    xmin = min(xs)
    xmax = max(xs)
    return (xmin, xmax)


print(min_max([0, 1, 2, 10, -5, 3]))

def geometric_mean(xs):
    product = 1
    for i in xs:
        product *= i
    mean = product ** (1 / len(xs))  # square root of len(xs)-th power
    return mean


print(geometric_mean([1, 2]))

def swing_time(L):
    return 2 * math.pi * math.sqrt(L / 9.81)


print(swing_time(1))

def range_squared(n):
    """A function range_squared(n) that takes an non-negative integer value
    n and returns the list [0, 1, 4, 9, 16, 25, ..., (n-1)^2]. If n is zero,
    the function should return the empty list."""
    if n > 0:
        return [i ** 2 for i in range(n)]
        # alternatively: return list(map(lambda x: x ** 2, range(n)))
    elif n == 0:
        return []
    else:
        return "Error: n must be zero or a positive integer."


print(range_squared(3))
print(range_squared(0))  # test if n is zero
print(range_squared(-1))  # test if n is a negative value

def count(element,seq):
    ans = 0
    for i in seq:
        if i == element:
            ans += 1
    return ans


print(count('dog', ['dog', 'cat', 'mouse', 'dog']))
print(count(2, list(range(5))))


