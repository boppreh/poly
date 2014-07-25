import unittest
from random import randint
from reference import Polynomial
from poly import *

def eval_naive_poly(coefs, x):
    result = 0
    for coef in coefs:
        result = coef + result * x
    return result

def randpoly(degree):
    return [randint(-10, 10) for d in range(degree + 1)]

class Tests(unittest.TestCase):
    def test_generate(self):
        for degree in range(2, 5):
            for i in range(100):
                poly = randpoly(degree)
                points = [(x, eval_naive_poly(poly, x)) for x in range(degree)]
                generator = generate(points, poly[0])
                for i in range(degree, degree + 10):
                    self.assertEqual(next(generator), eval_naive_poly(poly, i))

    def test_generate2(self):
        for i in range(100):
            poly = randpoly(2)
            points = [(x, eval_naive_poly(poly, x)) for x in range(1, 3)]
            generator = generate2(points, poly[0])
            for i in range(3, 10):
                self.assertEqual(next(generator), eval_naive_poly(poly, i))

    def test_eval2seq(self):
        for i in range(100):
            poly = randpoly(2)
            points = [(x, eval_naive_poly(poly, x)) for x in range(1, 3)]
            for i in range(20):
                x = randint(-100, 100)
                self.assertEqual(eval2seq(points, poly[0], x),
                                 eval_naive_poly(poly, x))

    def test_eval2(self):
        for i in range(100):
            poly = randpoly(2)
            x0 = randint(1, 100)
            xn = randint(1, 100)
            points = [(x0, eval_naive_poly(poly, x0)), (xn, eval_naive_poly(poly, xn))]

            for i in range(20):
                x = randint(-100, 100)
                self.assertEqual(eval2(points, poly[0], x), eval_naive_poly(poly, x))


if __name__ == '__main__':
    unittest.main()
