def build_adjacency_matrix(n, edges):

    adj_matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        adj_matrix[u - 1][v - 1] = 1

    return adj_matrix


if __name__ == '__main__':
    k, g = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(g)]

    adjacency_matrix = build_adjacency_matrix(k, edges)

    for row in adjacency_matrix:
        print(" ".join(map(str, row)))
