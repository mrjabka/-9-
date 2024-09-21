n = int(input())
n_numbers = list(map(int, input().split()))
x = int(input())
counter = 0

for num in n_numbers:
    if num == x:
        counter += 1

print(counter)
