n, k = map(int, input().split())
l = [int(input()) for i in range(n)]


def cut(a, b, length):

    left = 1
    right = max(length)
    result = 0

    while left <= right:

        mid = (left + right) // 2
        count = 0

        for l in length:
            count += l // mid

        if count >= b:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    print(cut(n, k, l))
