i = int(input())
list_i = list(map(int, input().split()))

j = int(input())
list_j = list(map(int, input().split()))

count_table = {}
for num in list_i:
    if num not in count_table:
        count_table[num] = 0
    count_table[num] += 1

output = []

for num in list_j:
    output.append(count_table.get(num, 0))

print(*output)
