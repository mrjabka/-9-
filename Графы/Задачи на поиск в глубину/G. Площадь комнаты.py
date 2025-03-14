def dfs(x, y, visited, grid, N):
    # Проверяем границы и является ли текущая клетка пустой и непосещенной
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if grid[x][y] == '*' or visited[x][y]:
        return 0

    # Помечаем текущую клетку как посещённую
    visited[x][y] = True
    area = 1  # Считаем текущую клетку в площадь

    # Проверяем все четыре направления
    area += dfs(x - 1, y, visited, grid, N)
    area += dfs(x + 1, y, visited, grid, N)
    area += dfs(x, y - 1, visited, grid, N)
    area += dfs(x, y + 1, visited, grid, N)

    return area


if __name__ == '__main__':
    N = int(input().strip())
    grid = [input().strip() for _ in range(N)]
    start_x, start_y = map(int, input().strip().split())

    start_x -= 1
    start_y -= 1

    visited = [[False] * N for _ in range(N)]

    room_area = dfs(start_x, start_y, visited, grid, N)

    print(room_area)
