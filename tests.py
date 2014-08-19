import unittest
from random import randint
from reference import Polynomial
from poly import *

class Tests(unittest.TestCase):
    def test_generate(self):
        for degree in range(2, 5):
            for i in range(100):
                poly = Polynomial.random(degree)
                points = poly.points(*range(degree))
                generator = generate(points, poly[-1])
                for i in range(degree, degree + 10):
                    self.assertEqual(next(generator), poly(i))

    def test_generate2(self):
        for i in range(100):
            poly = Polynomial.random(2)
            points = poly.points(1, 2)
            generator = generate2(points, poly[-1])
            for i in range(3, 10):
                self.assertEqual(next(generator), poly(i))

    def test_eval2seq(self):
        for i in range(100):
            poly = Polynomial.random(2)
            points = poly.points(*range(1, 3))
            for i in range(20):
                x = randint(-100, 100)
                self.assertEqual(eval2seq(points, poly[-1], x), poly(x))

    def test_eval2(self):
        for i in range(100):
            poly = Polynomial.random(2)
            x0 = randint(1, 100)
            xn = randint(1, 100)
            if x0 == xn:
                continue
            points = poly.points(x0, xn)

            for i in range(20):
                x = randint(-100, 100)
                if x in (x0, xn):
                    continue
                self.assertEqual(eval2(points, poly[-1], x), poly(x))


if __name__ == '__main__':
    unittest.main()
