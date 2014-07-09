import math

def eval2(n0, n1, c, at):
    return at * n1 - (at - 1) * n0 + math.factorial(at) * c

poly = lambda x: 2 * x ** 2 - 3 * x + 5
for i in range(1, 100):
    print(i, poly(i), eval2(poly(i-2), poly(i-1), 2, 2))


