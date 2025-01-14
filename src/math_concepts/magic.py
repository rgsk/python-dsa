from math import gcd

import numpy as np


def reduce_fraction(numerator, denominator):
    """
    Reduces a fraction to its shortest form.
    :param numerator: int, the numerator of the fraction
    :param denominator: int, the denominator of the fraction
    :return: tuple, the reduced numerator and denominator
    """
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


def lcm(*args):
    """
    Calculates the Least Common Multiple (LCM) of multiple integers.
    :param args: int, the numbers
    :return: int, the LCM of the numbers
    """
    if len(args) == 2:
        a, b = args
        return abs(a * b) // gcd(a, b)
    return lcm(args[0], lcm(*args[1:]))


def mean(numbers):
    return sum(numbers) / len(numbers)


def squared_mean(numbers):
    return sum([x**2 for x in numbers]) / len(numbers)


def variance(numbers):
    return (squared_mean(numbers) - mean(numbers)**2) / len(numbers)


def unbiased_variance(numbers):
    return (squared_mean(numbers) - mean(numbers)**2) / (len(numbers) - 1) * len(numbers)


def mean_deviation_form(numbers):
    mean_value = mean(numbers)
    return [x - mean_value for x in numbers]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def covariance_matrix(matrix):
    mean_deviation_value = [mean_deviation_form(row) for row in matrix]
    transposed_mean_deviation_value = transpose(mean_deviation_value)
    b_b_t = np.matmul(mean_deviation_value, transposed_mean_deviation_value)
    return b_b_t


def variance_x_fx(x, fx):
    n = len(x)
    ex2 = sum([x[i]**2 * fx[i] for i in range(n)])
    ex = sum([x[i] * fx[i] for i in range(n)])
    print(ex)
    return ex2 - ex**2


def cumulative(numbers):
    val = 0
    result = []
    for v in numbers:
        val += v
        result.append(val)
    return result


def cumulative_reverse(numbers):
    val = 0
    result = []
    for v in numbers[::-1]:
        val += v
        result = [val] + result
    return result


def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Returns the area of a triangle whose vertices are:
    (x1, y1), (x2, y2), (x3, y3).
    """
    return abs(x1*(y2 - y3) +
               x2*(y3 - y1) +
               x3*(y1 - y2)) / 2.0
