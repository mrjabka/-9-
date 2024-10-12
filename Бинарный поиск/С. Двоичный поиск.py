def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


n, k = map(int, input().split())
sorted_array = list(map(int, input().split()))
query_array = list(map(int, input().split()))

results = []
for number in query_array:
    if binary_search(sorted_array, number):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)

