def has_cycle(n, graph):
    color = [0] * n

    def dfs(v):
        if color[v] == 1:
            return True
        if color[v] == 2:
            return False

        color[v] = 1
        for u, is_connected in enumerate(graph[v]):
            if is_connected:
                if dfs(u):
                    return True

        color[v] = 2
        return False

    for i in range(n):
        if color[i] == 0:
            if dfs(i):
                return 1

    return 0


if __name__ == '__main__':
    n = int(input().strip())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

    result = has_cycle(n, adjacency_matrix)

    print(result)
