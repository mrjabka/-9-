def calculate_degrees(n, edges):
    in_degrees = [0] * n
    out_degrees = [0] * n

    for u, v in edges:
        out_degrees[u - 1] += 1
        in_degrees[v - 1] += 1

    return in_degrees, out_degrees


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    in_degrees, out_degrees = calculate_degrees(n, edges)

    for i in range(n):
        print(f'{in_degrees[i]}\n{out_degrees[i]}')
