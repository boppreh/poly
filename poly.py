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
    p1, p2 = points
    if p1 > p2:
        p1, p2 = p2, p1
    x1, y1 = p1
    x2, y2 = p2
    d = x - x2

    return (d + 1) * y2 - d * y1 + d * (d + 1) * c

if __name__ == '__main__':
    from reference import Polynomial
    p = Polynomial([10, 5, 3])
    print(p(10))
    print(p(11))
    #print(5 * p(11) - 8 * p(10) + 32 * 3)
    print(p(16), eval2([(10, p(10)), (11, p(11))], 3, 16))
    print(p(17), eval2([(10, p(10)), (11, p(11))], 3, 17))
    print(p(10), eval2([(14, p(14)), (15, p(15))], 3, 10))
