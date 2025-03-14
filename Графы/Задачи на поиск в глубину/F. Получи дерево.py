def dfs(node, parent, visited, tree_edges):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            tree_edges.append((node, neighbor))
            dfs(neighbor, node, visited, tree_edges)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    tree_edges = []

    dfs(1, -1, visited, tree_edges)

    for u, v in tree_edges:
        print(u, v)
        
