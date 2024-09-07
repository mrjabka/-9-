a, b, l, n = map(int, input().split())
n *= 2
print(a * (n - 1) + b * (n - 2) + l * 2)
