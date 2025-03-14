def is_transitive_graph(n, adjacency_matrix):

    for u in range(n):
        for v in range(n):
            if u != v and adjacency_matrix[u][v] == 1:
                for w in range(n):
                    if w != u and w != v:
                        # Если есть (u -> v) и (v -> w), но нет (u -> w), то граф не транзитивен
                        if adjacency_matrix[v][w] == 1 and adjacency_matrix[u][w] == 0:
                            return "NO"
    return "YES"


if __name__ == '__main__':
    n = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

    result = is_transitive_graph(n, adjacency_matrix)

    print(result)
