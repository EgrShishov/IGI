import math


def task1(x, eps):
    """
    Calculates arcsin with given accuracy
    :param x: float number between -1 and 1
    :param eps: accuracy, float
    :return: result and amount of iterations
    """

    n = 0
    result = 0.0
    try:
        an = math.factorial(2*n) * x ** (2*n + 1) / (4**n * math.factorial(n) ** 2 * (2*n + 1))
        result = an
        prev = .0
        while abs(an - prev) > eps:
            n += 1
            prev = an
            an = math.factorial(2*n) * x ** (2*n + 1) / (4**n * math.factorial(n) ** 2 * (2*n + 1))
            result += an
            if n == 500:
                print('Achieved max iteration!')
                break
    except (OverflowError, ValueError):
        print('Oops! Exception was caught')
    return result, n
