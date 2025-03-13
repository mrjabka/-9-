def find_sources_and_sinks(n, adjacency_matrix):

    sources = []
    sinks = []

    for i in range(n):
        in_degree = 0
        out_degree = 0

        for j in range(n):
            if adjacency_matrix[j][i] == 1:
                in_degree += 1
            if adjacency_matrix[i][j] == 1:
                out_degree += 1

        if in_degree == 0:
            sources.append(i + 1)
        if out_degree == 0:
            sinks.append(i + 1)

    return sources, sinks


if __name__ == '__main__':
    n = int(input())

    adjacency_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    sources, sinks = find_sources_and_sinks(n, adjacency_matrix)

    print(len(sources))
    print("\n".join(map(str, sources)))
    print(len(sinks))
    print("\n".join(map(str, sinks)))
