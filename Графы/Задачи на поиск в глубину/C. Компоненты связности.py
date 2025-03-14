def dfs(v, visited, graph, component):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            component.append(node)
            # Добавляем в стек всех непосещенных соседей
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)


def find_connected_components(n, edges):
    # Инициализируем граф как список смежности
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    components = []

    # Для каждой вершины запускаем DFS, если она не посещена
    for v in range(1, n + 1):
        if not visited[v]:
            component = []
            dfs(v, visited, graph, component)
            components.append(component)

    return components


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    components = find_connected_components(n, edges)

    print(len(components))
    for component in components:
        print(len(component))
        print(' '.join(map(str, component)))
