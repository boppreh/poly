from random import randint

class Polynomial(object):
    """
    Class for handling polynomials with overloaded operators.
    """
    @staticmethod
    def random(degree, min_coef=-10, max_coef=10):
        return Polynomial(randint(min_coef, max_coef) for d in range(degree +
            1))

    def __init__(self, coefs=()):
        """
        Creates a new polynomial with the given coefficients.
        The coefficients are given in a list in big endian form, starting with
        the constant term.
        """
        coefs = list(coefs)
        while coefs and coefs[-1] == 0:
            coefs.pop()

        self.coefs = coefs
        self.degree = len(self.coefs)

    def __getitem__(self, index):
        return self.coefs[index]

    def point(self, x):
        return (x, self(x))

    def points(self, *xs):
        return [self.point(x) for x in xs]

    def __add__(self, other):
        return Polynomial(c1 + c2 for c1, c2 in self._wrap_zip(other))

    def __radd__(self, other):
        return Polynomial(c2 + c1 for c1, c2 in self._wrap_zip(other))

    def __sub__(self, other):
        return Polynomial(c1 - c2 for c1, c2 in self._wrap_zip(other))

    def __rsub__(self, other):
        return Polynomial(c2 - c1 for c1, c2 in self._wrap_zip(other))

    def __mul__(self, other):
        other = other.coefs if isinstance(other, Polynomial) else [other]
        coefs = [0] * (len(self.coefs) + len(other))
        for i, c1 in enumerate(self.coefs):
            for j, c2 in enumerate(other):
                coefs[i + j] += c1 * c2

        return Polynomial(coefs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Polynomial):
            raise NotImplemented('Division of Polynomial by Polynomial is not yet implemented.')
        return Polynomial(c1 / other for c1 in self.coefs)

    def __truediv__(self, other):
        return self.__div__(other)

    def _naive_evaluation(self, x):
        power = 1
        total = 0
        for coef in self.coefs:
            total += power * coef
            power *= x

        return total

    def _horner_evaluation(self, x):
        result = self.coefs[-1]
        for coef in reversed(self.coefs[:-1]):
            result = coef + result * x

        return result

    def __call__(self, x):
        """
        Evaluates the Polynomial at `x`.
        """
        return self._horner_evaluation(x)

    def __repr__(self):
        """
        Prints the polynomial in the format 10x^0 + 5x^1 + 2x^2 + ...
        """
        return ' + '.join('{}x^{}'.format(coef, power) for power, coef in
                reversed(list(enumerate(self.coefs))))

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coefs == other.coefs
        else:
            return self.coefs == other

    def _wrap_zip(self, value):
        """
        Wraps the value in a polynomial with same degree.
        """
        if isinstance(value, Polynomial):
            return zip_longest(self.coefs, value.coefs, fillvalue=0)
        else:
            return zip_longest(self.coefs, [value], fillvalue=0)

