from sympy import Matrix, solve_linear_system, symbols
from sympy.simplify.simplify import simplify
from string import ascii_lowercase, ascii_uppercase

def build_formula(degree):
    xs = [symbols('x' + str(i)) for i in range(degree+1)]
    x = symbols('x')

    m = Matrix([[letter**power for letter in xs + [x]] for power in range(degree + 1)])

    factors = [symbols('f' + str(i)) for i in range(degree+1)]
    solutions = solve_linear_system(m, *factors)

    ys = [symbols('y' + str(i)) for i in range(degree+1)]
    final = sum(solutions[factors[i]] * ys[i] for i in range(degree + 1))
    return final
    #return simplify(final)


def eval_formula(formula, points, x):
    xs = [('x' + str(i), point[0]) for i, point in enumerate(points)]
    ys = [('y' + str(i), point[1]) for i, point in enumerate(points)]
    return formula.subs(xs + ys + [('x', x)])

formula1 = build_formula(1)
print('Generic formula (1):', formula1)
points = [(1, 10), (3, 24)]
print('p(0) =', eval_formula(formula1, points, 0)) # Expected 3

formula2 = build_formula(2)
print('Generic formula (2):', formula2)
points = [(1, 21), (30, 7329), (50, 20209)]
print('p(0) =', eval_formula(formula2, points, 0))

formula3 = build_formula(3)
print('Generic formula (3):', formula3)
points = [(1, 26), (3, 258), (10, 6929), (11, 9106)]
print('p(0) =', eval_formula(formula3, points, 0)) # Expected 9

formula4 = build_formula(4)
print('Generic formula (4):', formula4)
points = [(1, 25), (3, 773), (10, 76282), (11, 110805), (15, 375197)]
print('p(0) =', eval_formula(formula4, points, 0)) # Expected 2


from reference import Polynomial

def generate2(points):
    """
    Given p(x), p(x+1) and p(x+2) from a second degree polynomial,
    returns a generator of values p(x+3), p(x+4), etc.
    """
    p1, p2, p3 = [p[1] for p in points]
    while True:
        p4 = p1 - 3 * p2 + 3 * p3
        yield p4
        p1, p2, p3 = p2, p3, p4

def eval2_seq(points, x):
    """
    Given p(a), p(a+1) and p(a+2) from a second degree polynomial,
    returns p(x) from any given x.
    """
    p1, p2, p3 = [y for x, y in points]
    d = x - points[-1][0]
    return int(d * (d + 1) / 2) * p1 - d * (d + 2) * p2 + int((d + 1) * (d + 2) / 2) * p3

def eval2(points, x):
    a, b, c = [x for x, y in points]
    # DD + AB - AD - BD / (CC - BC + BA - AC)
    k = (x*x + a*b - a*x - b*x) / (c*c - b*c + b*a - a*c)
    j = (x - k*(c - a) - a) / (b - a)
    i = 1 - j - k

    print(i, j, k)
    p1, p2, p3 = [y for x, y in points]
    return i*p1 + j*p2 + k*p3


p = Polynomial.random(1)
points = p.points(1, 3)
print(p)
print(points)
print(p(0))
