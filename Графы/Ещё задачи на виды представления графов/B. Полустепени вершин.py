def calculate_degrees(n, adjacency_matrix):

    in_degrees = [0] * n
    out_degrees = [0] * n

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                out_degrees[i] += 1
                in_degrees[j] += 1

    return in_degrees, out_degrees


if __name__ == '__main__':
    n = int(input())

    adjacency_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    in_degrees, out_degrees = calculate_degrees(n, adjacency_matrix)

    for i in range(n):
        print(f'{in_degrees[i]}\n{out_degrees[i]}')
