a, b, c, d = map(int, input().split())

if (a == 1 and d == 1) or (a == 1 and c == 1) or (b == 1 and d == 1):
  print('YES')
else:
  print('NO')
