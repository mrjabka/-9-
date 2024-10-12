def min_questions(n):
    questions = 0
    range_size = 1

    while range_size < n:
        questions += 1
        range_size *= 2

    return questions


n = int(input().strip())
print(min_questions(n))
