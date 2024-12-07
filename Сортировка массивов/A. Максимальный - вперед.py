length = int(input())
mass = list(map(int, input().split()[:length]))


def replace(massive):

    t = massive.index(max(massive))
    massive[0], massive[t] = massive[t], massive[0]

    print(*massive)

    return None


if __name__ == '__main__':
    replace(mass)
