def calculate_degrees(matrix, n):
    degrees = []
    for i in range(n):
        degree = sum(matrix[i])
        degrees.append(degree)
    return degrees


if __name__ == '__main__':
    k = int(input())
    m = [list(map(int, input().split())) for _ in range(k)]

    vertex_degrees = calculate_degrees(m, k)

    print("\n".join(map(str, vertex_degrees)))
