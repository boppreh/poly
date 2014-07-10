import math

def generate(sequential_points, a):
    yield 1

def eval2(n0, n1, c, at):
    return at * n1 - (at - 1) * n0 + math.factorial(at) * c

if __name__ == '__main__':
    from tests import *
    unittest.main()
