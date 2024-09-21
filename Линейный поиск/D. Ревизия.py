n = int(input())
arr = list(map(int, input().split()))

max_value = arr[0]
max_index = 0

for i in range(1, n):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i

print(max_index + 1)
