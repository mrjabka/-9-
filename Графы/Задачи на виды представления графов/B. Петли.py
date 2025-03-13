def contains_loops(matrix, n):

    for i in range(n):
        if matrix[i][i] == 1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    k = int(input())
    m = [list(map(int, input().split())) for _ in range(k)]

    print(contains_loops(m, k))
