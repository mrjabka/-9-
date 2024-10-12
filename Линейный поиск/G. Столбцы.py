def check_columns_for_x(X, N, table):
    results = []

    for col in range(N):
        found = False
        for row in range(N):
            if table[row][col] == X:
                found = True
                break
        results.append("YES" if found else "NO")

    return results


X = int(input().strip())
N = int(input().strip())
table = [list(map(int, input().split())) for _ in range(N)]

results = check_columns_for_x(X, N, table)

for result in results:
    print(result)
