n = int(input())
numbers = [int(input()) for i in range(n)]


def sort(k, arr):

    if k % 2 == 0:
        numbers.sort(reverse=True)
    else:
        numbers.sort()

    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    for val in result:
        print(val)

    return None


if __name__ == '__main__':
    sort(n, numbers)

