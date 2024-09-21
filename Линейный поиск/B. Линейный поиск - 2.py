n = int(input())
n_numbers = list(map(int, input().split()))
x = int(input())

for num in n_numbers:
    if num == x:
        print('YES')
        exit()

print('NO')
