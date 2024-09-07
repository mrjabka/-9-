x = input()
y = []
for i in x:
    y.append(int(i))

y.sort()
if sum(y) != 0 and y.count(0) != 0:
    y[0] = y[y.count(0)]
    y[y.count(0) + 1] = 0

for i in y:
    print(i, end="")
