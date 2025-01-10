n = int(input())
numbers = [int(input()) for i in range(n)]


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def sort(k, arr):

    uniques = list(dict.fromkeys(arr))

    if k % 2 == 0:
        output = uniques
        for val in output:
            print(val)
    else:
        output = uniques[::-1]
        for val in output:
            print(val)

    return None


if __name__ == '__main__':
    sort(n, numbers)

