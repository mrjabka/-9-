def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add the remaining parts
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


if __name__ == '__main__':
    N = int(input().strip())
    numbers = []

    for _ in range(N):
        numbers.append(int(input().strip()))

    unique_numbers = list(set(numbers))

    sorted_numbers = merge_sort(unique_numbers)

    if N % 2 == 0:
        sorted_numbers.reverse()

    for num in sorted_numbers:
        print(num)
