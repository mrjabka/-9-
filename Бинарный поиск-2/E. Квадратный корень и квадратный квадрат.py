c = float(input())
eps = 1.0e-7


def solve(f, a, b):

    while b-a > eps:
        mid = (a + b) / 2
        y = f(mid)

        if y > c:
            b = mid
        else:
            a = mid

    return a


if __name__ == '__main__':
    result = solve(lambda x: x**2+x**0.5, 0, c)
    print('{:.7f}'.format(result))
