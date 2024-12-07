length = int(input())
mass = list(map(int, input().split()[:length]))
num, arg = input().split()


def append_num(massive, number, argument):
    output = []
    t0 = int(argument) - 1
    t1 = massive[0:t0]
    t2 = massive[t0:]

    output = t1 + [int(number)] + t2

    print(*output)

    return None


if __name__ == '__main__':
    append_num(mass, num, arg)
