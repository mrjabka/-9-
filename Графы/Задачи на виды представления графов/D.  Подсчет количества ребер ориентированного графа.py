def count_edges(matrix, n):
    total_edges = 0
    for i in range(n):
        for j in range(n):
            total_edges += matrix[i][j]

    return total_edges


if __name__ == '__main__':
    k = int(input())
    m = [list(map(int, input().split())) for _ in range(k)]

    print(count_edges(m, k))
