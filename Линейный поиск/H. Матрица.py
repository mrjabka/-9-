def count_saddle_points(matrix, n, m):
    count = 0

    for i in range(n):
        for j in range(m):
            current_value = matrix[i][j]
            is_row_min = all(current_value <= matrix[i][k] for k in range(m))
            is_col_max = all(current_value >= matrix[k][j] for k in range(n))

            if is_row_min and is_col_max:
                count += 1

    return count


n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for k in range(n)]


if __name__ == '__main__':
    print(count_saddle_points(matrix, n, m))
