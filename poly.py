import math

from fractions import Fraction
def choose(n, k): 
    """
    Returns the binomial coefficient indexed by n and k.
    """
    result = 1
    for i in range(k):
        result *= Fraction(n-i,i+1)
    return int(result)

def generate(sequential_points, a=0):
    """
    Given a list of points of length `d` and the coefficient of the
    largest power from a polynomial of degree `d`, returns a generator
    of the following points.
    """
    d = len(sequential_points)
    constant = math.factorial(d) * a
    ys = [y for x, y in sequential_points]
    while True:
        new_y = constant
        for i, y in enumerate(reversed(ys), 1):
            new_y -= (-1)**i * choose(d, i) * y
        yield new_y
        ys = ys[1:] + [new_y]

def long_step(ys, distance):
    """
    Given a list of the y values of equally spaced sorted x's, returns the y
    for the x `distance` spacings away from the first point.

    long_step([p(0), p(1), p(2)], 10) = p(10)
    long_step([p(x), p(x+2), p(x+4)], 10) = p(x + 10*2)
    """
    n = len(ys)
    while distance:
        for i in range(n - 1 + distance % 2):
            ys.append(sum((-1)**(i+n+1) * y * choose(n, i)
                          for i, y in enumerate(ys[-n:])))
        ys = ys[distance % 2::2]
        distance //= 2
    return ys[0]

def generate2(sequential_points, a):
    """
    Given two points from a second degree polynomial and the x^2 coefficient,
    returns a generator for the next points after the two given.
    """
    p1, p2 = sequential_points
    y1, y2 = p1[1], p2[1]

    constant = 2 * a
    while True:
        y3 = 2 * y2 - y1 + constant
        yield y3
        y2, y1 = y3, y2

def eval2(points, c, x):
    """
    Given two points from a second degree polynomial and the x^2 coefficient,
    returns the point at p(x).
    """
    p1, pn = points
    if p1 > pn:
        p1, pn = pn, p1
    x1, y1 = p1
    xn, yn = pn
    d = xn - x1 - 1

    x2 = x1 + 1
    y2 = (d * y1 - d * (d + 1) * c + yn) / (d + 1)
    points = [(x1, y1), (x2, y2)]
    return eval2seq(points, c, x)

def eval2seq(points, c, x):
    """
    Given two *sequential* points from a second degree polynomial and the x^2
    coefficient, returns the point at p(x).
    """
    p1, p2 = points
    if p1 > p2:
        p1, p2 = p2, p1
    x1, y1 = p1
    x2, y2 = p2
    d = x - x2

    return (d + 1) * y2 - d * y1 + d * (d + 1) * c

if __name__ == '__main__':
    from reference import Polynomial
    p = Polynomial([10, 5])
    print(jump([p(0), p(1)], 5), p(5))

    p = Polynomial([10, 5, 2])
    print(jump([p(1), p(3), p(5)], 5), p(11))

    p = Polynomial([10, 5, 2, 1])
    print(jump([p(1), p(3), p(5), p(7)], 5), p(11))
