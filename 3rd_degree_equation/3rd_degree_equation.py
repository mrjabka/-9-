polinome = list(map(int, input().split())) # коэффициенты при переменной

def neg_or_pos(x):  # Определяем знак принимаемого числа

    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def rational_solve(func, a, b, eps = 1.0e-14): # Ищем единственный вещественный корень с точностью eps

    func_a = func(a)
    func_b = func(b)

    while True:
        c = (a + b) / 2  # mid значение

        if abs(b - a) < eps:
            return c

        func_c = func(c)

        if abs(func_c) <= eps:
            return c

        if neg_or_pos(func_a)*neg_or_pos(func_c)<0:
            b = c
            func_b = func_c
        else:
            a = c
            func_a = func_c


def div(p, a):  # Получаем квадратный полином методом Горнера

    r = [0, 0, 0]
    r[2] = p[3]  # p[3] - свободный коэффициент полинома
    r[1] = p[2]+a*p[3]
    r[0] = (p[1]+a*(p[2]+a*p[3]))

    return tuple(r)


def solve_equation(p):

    q = max(p)
    left = -abs(q)/abs(p[3])
    right = -left

    x1 = rational_solve(lambda x: p[3]*x**3+p[2]*x**2+p[1]*x+p[0],left,right)
    (c, b, a) = div(p, x1)
    d = b**2-4*a*c
    x2 = (-b-d**0.5)/(2*a)
    x3 = (-b+d**0.5)/(2*a)

    return (x1, x2, x3)

if __name__ == '__main__':
  print(solve_equation(polinome))
