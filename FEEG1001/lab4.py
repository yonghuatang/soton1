# Lab 4 (Online Lab)
# 02 November 2020
# © TangYongHua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import math
import urllib.request

# Question 1

def seq_sqrt(xs):
    """A function seq_sqrt(xs) which takes a list of non-negative numbers xs with elements
    [x0, x1, x2, ..., xn], and returns the list [sqrt(x0), sqrt(x1), sqrt(x2), ..., sqrt(xn)].
    In other words, the function takes a list of numbers, and returns a list of the same length
    that contains the square root for each number in the list."""
    return list(map(lambda x: math.sqrt(x), xs))


# Question 2

def mean(xs):
    """A function mean(xs) that takes a sequence xs of numbers, and returns the (arithmetic) mean
    (i.e. the average value)."""
    count = 0
    for i in xs:
        count += i
    return count / len(xs)


# Question 3

def noaa_string():
    """A function noaa_temperature(s) which should take a string s as returned from noaa_string()
    as the input argument, extract the temperature in degree Celsius from the string, and return
    this temperature as an integer number."""
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


def noaa_temperature(s):
    s = noaa_string().split('\n')
    return s[6][-5:-3]  # [inclusive:exclusive]

print(noaa_temperature(noaa_string()))

# Question 4

def wc(filename):
    """A function wc(filename) that returns the number of words in file filename.
    The name wc stands for Word Count."""
    f = open(filename, 'rt')
    content = f.read()
    f.close()
    return len(content.split())


# Question 5

def line_averages(filename):
    """A function line_averages(filename) that takes a string filename
    which contains the name of a file to be processed. The function should
    compute the average value for every line, and return the average values in a list."""
    f = open(filename, 'rt')
    data = f.read()
    f.close()
    values = data.split('\n')
    result = []
    for i in values:
        result.append(mean(i))
    return result


# Question 6

def count_sub_in_file(filename,s):
    """Write a function count_sub_in_file(filename,s) that takes two arguments:
    the substring s (of type string) and a filename (of type string). The function
    should return the number of occurrences of s in the file given through filename."""
    f = open(filename, 'rt')
    data = f.read()
    f.close()
    return data.count(s)
