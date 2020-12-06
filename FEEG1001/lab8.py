# Lab 8 (Online Lab)
# 30 November 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import numpy as np
import scipy
import matplotlib.pyplot as plt

def trapez(f, a, b, n):
    h = (b - a) / n
    x_data = np.linspace(a, b, n+1)  # need n+1 points to define n subdivisions!
    y_data = list(map(f, x_data))
    weight = np.ones(n+1)
    weight[1:-1] = 2
    area = (h / 2) * np.dot(y_data, weight)
    return area


def finderror(n):
    def g(x):
        return (x ** 3) / 3
    error = trapez(lambda x: x * x, -1, 2, n) - (g(2) - g(-1))
    return error


def using_quad():
    return scipy.integrate.quad(lambda x: x ** 2, -1, 2)

def f1(x):
    return np.cos(2 * np.pi * x) * np.exp(-x ** 2)


def f2(x):
    return np.log(x + 2.2)


def create_plot_data(f, xmin, xmax, n):
    xs = np.linspace(xmin, xmax, n)
    ys = [f(x) for x in xs]
    return (xs, ys)


def myplot():
    values1 = create_plot_data(f1, -2, 2, 1001)
    values2 = create_plot_data(f2, -2, 2, 1001)
    def g(x):
        return f1(x) - f2(x)
    values3 = create_plot_data(g, -2, 2, 1001)
    plt.plot(values1[0], values1[1], label='f1')
    plt.plot(values2[0], values2[1], label='f2')
    plt.plot(values3[0], values3[1], label='f1-f2')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    plt.savefig('plot.jpg')
    plt.savefig('plot.pdf')


def find_cross():
    # To find f1 = f2, i.e. f1 - f2 = 0
    def fnew(x):
        return f1(x) - f2(x)
    return scipy.optimize.brentq(fnew, 0, 2)
