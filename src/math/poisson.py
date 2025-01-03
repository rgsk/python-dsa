import math


def poisson_pmf(lambda_value, x):
    """
    Calculate the Poisson PMF.

    Parameters:
    - lambda_value (float): The expected number of occurrences (λ).
    - x (int): The actual number of occurrences.

    Returns:
    - float: The probability of observing x occurrences.
    """
    return (lambda_value ** x) * math.exp(-lambda_value) / math.factorial(x)


def poisson_range(lambda_value, start, end):
    result = 0
    for x in range(start, end + 1):
        result += poisson_pmf(lambda_value, x)
    return result
