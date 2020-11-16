# Lab 6 (Online Lab)
# 16 November 2020
# © Tang Yong Hua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import math

def positive_places(f, xs):
    """Takes as arguments some function f and a list of numbers xs and returns a list
     of those-and-only-those elements x of xs for which f(x) is strictly greater than
     zero. """

    ans = []
    for x in xs:
        if f(x) > 0:
            ans.append(x)
    return ans


def eval_f_0123(f):
    """Evaluates the function f=f(x) at positions x=0, x=1, x=2 and x=3. The function should return
     the list [f(0), f(1), f(2), f(3)]."""

    return [f(x) for x in range(0, 4)]  # [inclusive, exclusive]


def eval_f(f, xs):
    """Takes a function f = f(x) and a list xs of values that should be used as arguments for f.
     The function eval_f should apply the function f subsequently to every value x in xs, and
    return a list fs of function values. I.e. for an input argument xs=[x0, x1, x2,..., xn] the
    function eval_f(f, xs) should return [f(x0), f(x1), f(x2), ..., f(xn)]."""

    return [f(x) for x in xs]
    # alternatively: return list(map(f, xs))


def sum_f(f, xs):
    """ Returns the sum of the function values of f evaluated at values x0, x1, x2, ..., xn
     where xs=[x0,x1,x2,...,xn]."""

    ans = 0
    for x in xs:
        ans += f(x)
    return ans


def std_dev(x):
    """Takes a list x of floating point numbers, and computes and returns the corrected sample
     standard deviation of the floating point numbers in the list x."""

    import statistics
    return statistics.stdev(x)



