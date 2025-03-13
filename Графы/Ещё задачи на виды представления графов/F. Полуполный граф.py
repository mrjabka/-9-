def is_semi_complete_graph(n, edges):

    edge_set = set()

    for u, v in edges:
        edge_set.add((u, v))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if (i, j) not in edge_set and (j, i) not in edge_set:
                    return "NO"

    return "YES"


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = is_semi_complete_graph(n, edges)

    print(result)
