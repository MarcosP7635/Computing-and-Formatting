'''
The purpose of this file is to have a set of functions that can calculate
error propagation.
All inputs will be dictionaries of the form
dict = {value1: uncertainty1, value2: uncertainty2, ...}
All outputs will be lists of the form (value, uncertainty).
All uncertanties should be listed as nonnegative real numbers.
For the general() function to calculate the exact uncertainty,
the syntax for defining functions used here:
https://www.askpython.com/python/examples/derivatives-in-python-sympy
should be used.
The purpose of symbol_list list is to have up to 26 variable names to take
partial differentials in general()
All functions used in the general function must use the first n letters of
the alphabet as their variables
'''

import sympy as sym
import math
from sympy import *
import numpy as np


a, b, c, d, e, f, g, h, i, j, k, l, m = sym.symbols('a b c d e f g h i j k l m')
n, o, p, q, r, s, t, u, v, w, x, y, z = sym.symbols('n o p q r s t u v w x y z')
symbol_list = (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v,
w, x, y, z)


def sum (dict):
    keys = np.array(list(dict.keys()))
    values = np.array(list(dict.values()))
    best_est = np.sum(keys)
    uncertainty = np.sum(values)
    return (best_est, uncertainty)

def product (dict):
    keys = np.array(list(dict.keys()))
    values = np.array(list(dict.values()))
    best_est = np.prod(keys)
    uncertainty = 0
    for index in range(len(values)):
        uncertainty += values[index] / np.abs(keys[index])
    uncertainty *= np.abs(best_est)
    return (best_est, uncertainty)

def power (dict, exponent):
    #where exponent is the exponent or an array of exponents,
    #must be of the same length as the number of unique keys in dict
    try:
        if not isinstance(n, np.ndarray):
            exponent = np.array(list((n)))
    except TypeError:
        exponent = np.array(n) #only one exponent entered
    keys = np.array(list(dict.keys()))
    values = np.array(list(dict.values()))
    best_est = np.power(keys, exponent)
    uncertainty = np.abs(best_est) * exponent * values / np.abs(keys)
    return ("best estimate(s): ", best_est, "\n uncertainties: ", uncertainty)

def general_with_arrays(expectation_values, uncertainties, fun, print_fun=False, print_sum_squares=False):
    #can only take up to 26 inputs, but allows different inputs to have the same expectation value
    #its output is of the form (exact uncertainty, maximum uncertainty)
    #the input is an array of dictionaries, where each input gets its own dictionary
    #the keys are the expectation value and the values are the uncertainty (standard deviation)
    sum_squares = 0
    keys, values = expectation_values, uncertainties
    for index in range(len(keys)):
        f = fun.diff(symbol_list[index])
        lam_f = lambdify(symbol_list[0:len(keys)], f)
        sum_squares += (lam_f(*keys) * values[index]) ** 2
        if print_sum_squares:
            print(sum_squares)
    lam_og = lambdify(symbol_list[0:len(keys)], fun)
    best_est = lam_og(*keys)
    if print_fun:
        print(fun)
    uncertainty = math.sqrt(sum_squares)
    return (best_est, uncertainty)


def general (dict, fun):
    #can only take up to 26 inputs
    #its output is of the form (exact uncertainty, maximum uncertainty)
    sum_squares = 0

    try:
        keys = np.array(list(dict.keys()))
        values = np.array(list(dict.values()))
        for index in range(len(keys)):
            f = fun.diff(symbol_list[index])
            lam_f = lambdify(symbol_list[0:len(keys)], f)
            sum_squares += (lam_f(*keys) * values[index]) ** 2
            print(sum_squares)
        lam_og = lambdify(symbol_list[0:len(keys)], fun)
        best_est = lam_og(*keys)
        print(fun)

    except:
        print("Singular uncertainty entered")
        keys = list(dict.keys())
        keys = float(keys[0])
        values = list(dict.values())
        values = float(values[0])
        f = fun.diff(symbol_list[0])
        lam_f = lambdify(symbol_list[0], f)
        sum_squares += (lam_f(keys) * values) ** 2
        lam_og = lambdify(symbol_list[0], fun)
        lam_og(keys)

    uncertainty = math.sqrt(sum_squares)

    return (best_est, uncertainty)
#a = x, y = b, c = theta
fun = (a + 2) / (a + (b * cos(4 * c * pi / 180)))
dict = {10:2, 7:1, 40:3}
print(general(dict, fun))