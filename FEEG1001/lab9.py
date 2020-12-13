# Lab 9 (Online Lab)
# 07 December 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, newton

# Question 1

def model(t, Ti, Ta, c):
    temperature = (Ti - Ta) * np.exp(-t / c) + Ta
    return temperature


# Question 2

def read2coldata(filename):
    with open(filename, 'rt') as f:
        data = f.read()
        f.close()
    a_temp = data.split()[0::2]
    b_temp = data.split()[1::2]
    def str_to_float(list):
        """Convert each string elements in list into floating point numbers."""
        new_list = []
        for str in list:
            new_list.append(float(str))
        return new_list
    a = np.array(str_to_float(a_temp))  # converts string into float and then numpy array
    b = np.array(str_to_float(b_temp))
    return (a, b)  # returns a tuple


# Question 3

def extract_parameters(ts, Ts):
    p, pcov = curve_fit(model, ts, Ts)
    Ti, Ta, c = p
    return tuple(Ti, Ta, c)


def plot(ts, Ts, Ti, Ta, c):
    plt.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    plt.plot(ts, fTs, label='fitted')
    plt.legend()
    plt.show()


plot(ts, Ts, Ti, Ta, c)

# Question 4

def sixty_degree_time():
    time, temperature = read2coldata('lab9_data.txt')
    Ti, Ta, c = extract_parameters(time,temperature)
    ans = newton(lambda t: model(t, Ti, Ta, c) - 60, 0, tol=1e-16)  # function and initial guess
    return ans
