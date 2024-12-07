length = int(input())
mass = list(map(int, input().split()[:length]))


def bubble_sort(massive):
    n = len(massive)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if massive[j] > massive[j+1]:
                massive[j], massive[j+1] = massive[j+1], massive[j]
                swapped = True

        if not swapped:
            break

    print(*massive)

    return None


if __name__ == '__main__':
    bubble_sort(mass)
