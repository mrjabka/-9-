import math


def min_questions(N):
    return math.ceil(math.log2(N))


N = int(input().strip())
print(min_questions(N))
