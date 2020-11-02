# Lab 4 (Online Lab)
# 02 November 2020
# © TangYongHua
# Code available on Github https://github.com/yonghuatang/soton1/tree/master/FEEG1001
# Python version 3.8

import math
import urllib.request

# Question 1

def seq_sqrt(xs):
    return list(map(lambda x: math.sqrt(x), xs))

my_list = [1, 2, 3, 4, 5]
print(seq_sqrt(my_list))

# Question 2

def mean(xs):
    count = 0
    for i in xs:
        count += i
    return count / len(xs)


print(mean([0, 1, 2]))

# Question 3

def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


print(noaa_string())

# Question 4

def noaa_temperature(s):
    s = noaa_string().split('\n')
    return s[6][-5:-3]  # [inclusive:exclusive]

print(noaa_temperature(noaa_string()))

# Question 5

def wc(filename):
    f = open(filename, 'rt')
    content = f.read()
    f.close()
    return len(content.split())


print(wc(r"C:\Users\tangy\AppData\Local\Programs\Python\Python38\lab4_data.txt"))

# Question 6

def line_averages(filename):
    f = open(filename, 'rt')
    data = f.read()
    f.close()
    values = data.split('\n')
    result = []
    for i in values:
        result.append(mean(i))
    return result

# Question 7

def count_sub_in_file(filename,s):
    f = open(filename, 'rt')
    data = f.read()
    f.close()
    return data.count(s)
