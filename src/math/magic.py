from math import gcd


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
