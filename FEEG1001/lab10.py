# Lab 10 (Online Lab)
# 14 December 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, odeint
from scipy.interpolate import interp1d
from scipy.optimize import fmin

# Question 1

def f(x):
    return (np.exp(-(x**2)) / (1+(x**2))) + ((2*(np.cos(x)**2)) / (1+(x-4)**2))


# Question 2

def integrate_f_from0(b):
    return quad(f, 0, b)


# Question 3

def find_max_f():
   def negative_f(x):
       return -f(x)
   ans = fmin(negative_f, 0, xtol=1e-16)
   print('\n')
   return float(ans)



# Question 4

def make_multiplier(factor):
    def wrapper(x):
        return x * factor
    return wrapper


# Question 5

def lin_int(xs, ys):
    fbar = interp1d(xs, ys, kind='linear')
    def f(x):
        return fbar(x)
    return f


# Question 6

def make_oscillator(frequency):
    def wrapper(t):
        return np.sin(t * frequency)
    return wrapper


# Question 7 & 8

def solve_freefall(ts, v0, m=80):
    A = 0.5
    c = 0.25
    g = 9.81
    vs = odeint(lambda v, t: g - (A * c * v**2 / m), v0, ts)
    return vs

# Just a exemplary implementation and plotting of the function
ts = np.arange(0, 101, 1)  # (inclusive, exclusive, step)
plt.plot(ts, solve_freefall(ts, v0=0), 'x', label=r'$\frac{dv}{dt}=g-\frac{Ac}{m}v^2$')  # LaTeX environment
plt.xlabel('t')
plt.ylabel('v')
plt.grid()
plt.legend()
plt.show()
