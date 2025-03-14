def can_be_seated(n, m, dislike_pairs):

    graph = [[] for _ in range(n + 1)]
    for u, v in dislike_pairs:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)

    def bfs(start):
        queue = [start]
        colors[start] = 1
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False

        return True

    for v in range(1, n + 1):
        if colors[v] == 0:
            if not bfs(v):
                return "NO"

    table1 = [i for i in range(1, n + 1) if colors[i] == 1]
    return f"YES\n{' '.join(map(str, table1))}"


if __name__ == '__main__':
    n, m = map(int, input().split())
    dislike_pairs = [tuple(map(int, input().split())) for _ in range(m)]

    result = can_be_seated(n, m, dislike_pairs)

    print(result)
