def calculate_degrees(n, edges):

    degrees = [0] * n

    for u, v in edges:
        degrees[u - 1] += 1
        degrees[v - 1] += 1

    return degrees


# Ввод данных
n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

degrees = calculate_degrees(n, edges)

print('\n'.join(map(str, degrees)))
