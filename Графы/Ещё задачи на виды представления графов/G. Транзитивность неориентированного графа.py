def is_transitive_graph(n, edges):
    edge_set = set()

    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))

    for u, v in edges:
        for w in range(1, n + 1):
            if w != u and w != v:
                if ((v, w) in edge_set or (w, v) in edge_set) and not ((u, w) in edge_set or (w, u) in edge_set):
                    return "NO"

    return "YES"


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = is_transitive_graph(n, edges)

    print(result)
