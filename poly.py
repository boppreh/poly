import math

from fractions import Fraction
def choose(n, k): 
    result = 1
    for i in range(k):
        result *= Fraction(n-i,i+1)
    return int(result)

def generate(sequential_points, a):
    d = len(sequential_points)
    constant = math.factorial(d) * a
    while True:
        total = 0
        for i, point in enumerate(sequential_points, start=1):
            part = choose(d, i) * point[1]
            if i % 2:
                total -= part
            else:
                total += part
        yield total + constant

def generate2(sequential_points, a):
    p1, p2 = sequential_points
    y1, y2 = p1[1], p2[1]

    constant = 2 * a
    while True:
        y3 = 2 * y2 - y1 + constant
        yield y3
        y2, y1 = y3, y2

def eval2(points, c, x):
    at = x - points[0][0]
    nat = points[1][1]
    n0 = points[0][1]
    points[1] = (nat + (at - 1) * n0 - math.factorial(at) * c) / -at
    return eval2seq(points[0], points[1], c, x)

def eval2seq(points, c, at):
    n0, n1 = points[0][1], points[1][1]
    return at * n1 - (at - 1) * n0 + math.factorial(at) * c

if __name__ == '__main__':
    from tests import *
    unittest.main()
