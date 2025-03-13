def is_regular_graph(n, edges):

    degrees = [0] * n

    for u, v in edges:
        degrees[u - 1] += 1
        degrees[v - 1] += 1

    first_degree = degrees[0]
    for degree in degrees:
        if degree != first_degree:
            return "NO"

    return "YES"


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = is_regular_graph(n, edges)

    print(result)
