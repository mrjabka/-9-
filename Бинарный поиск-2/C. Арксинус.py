from math import sin, pi

a = float(input())
x = 0

left = - pi / 2
right = pi / 2

eps = 1.0e-7


if __name__ == '__main__':

    while right - left > eps:

        mid = (left + right) / 2

        if sin(mid) < a:
            left = mid
        else:
            right = mid

    print(left)
