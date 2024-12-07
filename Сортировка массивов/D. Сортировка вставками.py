length = int(input())
mass = list(map(int, input().split()[:length]))


def insert_sort(massive):
    output = []

    for i in range(len(massive)):
        output.append(min(massive))
        massive.remove(min(massive))

    print(*output)

    return None


if __name__ == '__main__':
    insert_sort(mass)
