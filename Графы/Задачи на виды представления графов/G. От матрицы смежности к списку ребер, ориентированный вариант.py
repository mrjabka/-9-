def get_edge_list(matrix, n):
    edge_list = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edge_list.append((i + 1, j + 1))
    return edge_list


if __name__ == '__main__':
    k = int(input())
    m = [list(map(int, input().split())) for _ in range(k)]

    edges = get_edge_list(m, k)

    for edge in edges:
        print(edge[0], edge[1])
