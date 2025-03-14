def dfs(graph, visited, vertex):
    stack = [vertex]
    count = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            count += 1
            # Добавляем в стек все смежные, но еще не посещенные вершины
            for i, connected in enumerate(graph[v]):
                if connected and not visited[i]:
                    stack.append(i)

    return count


if __name__ == '__main__':
    n, s = map(int, input().split())
    s = s - 1

    adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    count = dfs(adjacency_matrix, visited, s)

    print(count)
