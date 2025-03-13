def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()[:n]))

    sorted_array = quicksort(array)

    print(" ".join(map(str, sorted_array)))
