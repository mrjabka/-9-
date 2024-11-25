n = int(input()) # размер матрицы

def arr(k):

    array = [[-1 for i in range(n)] for j in range(n)]

    for l in range(n):
        array[l][l] = n - l

    for row in array:
        print(row)

    return None

if __name__ == '__main__':
    arr(n)
