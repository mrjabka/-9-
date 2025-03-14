def count_connected_components(M, N, grid):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(x, y):

        return 0 <= x < M and 0 <= y < N and grid[x][y] == '#'

    def dfs(x, y):
        # Стек для DFS
        stack = [(x, y)]
        grid[x][y] = '.'
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny):
                    grid[nx][ny] = '.'
                    stack.append((nx, ny))

    count = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                dfs(i, j)
                count += 1

    return count


if __name__ == '__main__':
    M, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(M)]

    result = count_connected_components(M, N, grid)

    print(result)
