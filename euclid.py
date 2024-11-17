a = int(input())
b = int(input())

if __name__ == '__main__':
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    print(a+b)
