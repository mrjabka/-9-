def find_closest(arr, target):
    low, high = 0, len(arr) - 1

    if target <= arr[low]:
        return arr[low]

    if target >= arr[high]:
        return arr[high]

    while low < high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    if abs(arr[low] - target) < abs(arr[low - 1] - target):
        return arr[low]

    return arr[low - 1]


n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for x in arr_k:
    print(find_closest(arr_n, x))
