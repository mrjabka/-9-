def is_valid_adjacency_matrix(matrix, n):

    for i in range(n):
        if matrix[i][i] != 0:
            return "NO"

        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    k = int(input())
    m = [list(map(int, input().split())) for _ in range(k)]

    print(is_valid_adjacency_matrix(m, k))
