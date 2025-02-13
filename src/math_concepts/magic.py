import math
from math import gcd

import matplotlib.pyplot as plt
import numpy as np
from sympy import Rational, diff, simplify  # type:ignore


def C(n, r):
    if r == 0:
        return 1
    if r > n // 2:
        return C(n, n - r)
    return n * C(n - 1, r - 1) // r


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


def projxS(A, x):
    # projection of x on subspace S spanned by linearly independent vectors {a1, a2}
    A = np.array(A)
    x = np.array(x)
    return A @ np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ x


def distxS(A, x):
    x = np.array(x)
    return np.linalg.norm(np.array(x) - projxS(A, x))


def angle(u, v):
    # find the angle between two vectors u and v
    u = np.array(u)
    v = np.array(v)
    c = np.dot(u, v)/np.linalg.norm(u) / \
        np.linalg.norm(v)  # -> cosine of the angle
    return np.degrees(np.arccos(c))


def anglexS(A, x):
    return angle(x, projxS(A, x))


def least_squares_solution(A, b):
    A = np.array(A)
    b = np.array(b)
    return np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ b


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


def bernoulli_trial(n, r, p=None, p_not=None):
    if p is None and p_not is None:
        raise Exception('Either p or p_not should be defined')
    if p is None:
        p = 1 - p_not
    if p_not is None:
        p_not = 1 - p
    return C(n, r) * p ** r * (p_not) ** (n - r)


def binomial_distribution(n, start, end, p=None, p_not=None):
    ans = 0
    for i in range(start, end + 1):
        ans += bernoulli_trial(n, i, p, p_not)
    return ans


def geometric_pmf(p, x):
    """
    Calculate the Geometric PMF.

    Parameters:
    - p (float): The probability of success in a single trial.
    - x (int): The number of trials until the first success.

    Returns:
    - float: The probability of observing x trials until the first success.
    """
    return p * (1 - p) ** (x - 1)


def geometric_distribution(p, start, end):
    result = 0
    for x in range(start, end + 1):
        result += geometric_pmf(p, x)
    return result


def convert_to_rational(expr):
    """
    Converts all numerical coefficients in a SymPy expression to rational numbers.

    Parameters:
        expr: sympy.Expr
            The input expression.

    Returns:
        sympy.Expr
            The expression with all numerical coefficients as Rational numbers.
    """
    if expr.is_Atom:  # Base case: if it's a single term
        if expr.is_Number:
            return Rational(expr)
        return expr

    if expr.is_Add or expr.is_Mul:  # If it's an addition or multiplication
        return expr.func(*[convert_to_rational(arg) for arg in expr.args])

    if expr.is_Pow:  # If it's a power
        base, exp = expr.args
        return base**convert_to_rational(exp)

    return expr  # Default case: return as is


def quadratic_taylor_multivariable(f, vars, point):
    """
    Compute the quadratic Taylor expansion of a multivariable function 
    at a given point.

    Parameters:
    - f:      The sympy expression representing the function.
    - vars:   A list of sympy symbols [x1, x2, ..., xn].
    - point:  A dict {x1: a1, x2: a2, ...} giving the expansion point.

    Returns:
    - The quadratic Taylor expansion of f about 'point', simplified.
    """

    # 0th-order term:  f(a)
    taylor = f.subs(point)

    # 1st-order terms:  sum of df/dx_i (a) * (x_i - a_i)
    for v in vars:
        df_dv = diff(f, v)
        taylor += df_dv.subs(point) * (v - point[v])

    # 2nd-order terms:
    #    1/2 \sum_{i,j} f_{i j}(a) * (x_i - a_i)(x_j - a_j)
    # A common way to avoid double counting is to loop i <= j:
    n = len(vars)
    for i in range(n):
        for j in range(i, n):
            d2 = diff(f, vars[i], vars[j]).subs(point)
            if i == j:
                # pure second derivative terms get a 1/2 factor
                taylor += d2 * (vars[i] - point[vars[i]])**2 / 2
            else:
                # cross terms appear once, but with no 1/2
                # (because f_{xy} = f_{yx} for sufficiently smooth f)
                taylor += d2 * (vars[i] - point[vars[i]]) * \
                    (vars[j] - point[vars[j]])

    return convert_to_rational(simplify(taylor))


def generate_factors(n: int):
    lf = []
    rf = []
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            lf.append(i)
            if i * i != n:
                rf.append(n // i)
    return lf + rf[::-1]


def plot_function(func, x_range=(-10, 10), num_points=1000, asymptotes=None, ylim=(-10, 10)):
    """
    Plots an arbitrary function with optional vertical asymptotes.

    Parameters:
    - func: The function to be plotted (should take a numpy array as input).
    - x_range: Tuple specifying the range of x values (default: (-10, 10)).
    - num_points: Number of points to generate for smooth plotting (default: 1000).
    - asymptotes: List of x-values where vertical asymptotes occur (default: None).
    - ylim: Tuple specifying the y-axis limits to control the view.
    """
    x = np.linspace(x_range[0], x_range[1], num_points)
    if asymptotes:
        for a in asymptotes:
            # Remove points near asymptotes to avoid discontinuities
            x = x[np.abs(x - a) > 0.05]

    y = func(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Function Graph", color='b')

    if asymptotes:
        for a in asymptotes:
            plt.axvline(x=a, color='r', linestyle='dashed',
                        label=f'Asymptote at x={a}')

    plt.axhline(y=0, color='black', linewidth=1)
    plt.ylim(ylim)
    plt.xlim(x_range)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the Given Function')
    plt.legend()
    plt.grid(True)
    plt.show()
