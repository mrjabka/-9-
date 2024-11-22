a = float(input())
n = int(input())
val = 0

if __name__ == '__main__':
    if a < 1:
        r = 1
    else:
        r = a

    m = r / 2

    for i in range(200):
        if m ** n >= a:
            r = m
        else:
            val = m
        m = (val + r) / 2

    print(r)
