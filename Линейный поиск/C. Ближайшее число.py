def find_closest_element(arr, target):
    closest = arr[0]
    min_diff = abs(arr[0] - target)

    for num in arr[1:]:
        diff = abs(num - target)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return closest

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

result = find_closest_element(arr, x)
print(result)
