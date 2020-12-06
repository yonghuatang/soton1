# Lab 7 (Online Lab)
# 23 November 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import math
import numpy as np
from scipy.optimize import bisect

# Question 1 & 2

def derivative(f, x0, eps=1e-6):
    """Computes a numerical approximation of the first derivative of the function f(x)
     at the point x0 using central differences."""

    e = 1e-6

    return ((f(x0 + (eps/2))) - (f(x0 - (eps/2)))) / eps


# Question 3 & 4

def newton(f, x0, feps, maxit):
    iter_count = 0
    while abs(f(x0)) > feps:
        if iter_count >= maxit:
            raise RuntimeError(f"Failed after {iter_count} iterations.")
            break
        else:
            x0 = x0 - f(x0) / derivative(f, x0)  # overwrite the previous value
            iter_count += 1
    return x0


# Question 5

def y(x):
    return (np.exp(-(x**2)) / (1+(x**2))) + ((2*(np.cos(x)**2)) / (1+(x-4)**2))


# Question 6

def find_y_equals_1(y):
    def y_prime(x):
        return y(x) - 1
    from scipy.optimize import bisect
    return bisect(y_prime, -1, 0)






