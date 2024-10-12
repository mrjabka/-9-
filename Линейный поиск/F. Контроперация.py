def replace_max_with_min(grades):
    if len(grades) == 0:
        return grades

    max_grade = max(grades)
    min_grade = min(grades)

    for i in range(len(grades)):
        if grades[i] == max_grade:
            grades[i] = min_grade

    return grades


n, *grades = map(int, input().split())

corrected_grades = replace_max_with_min(grades)

print(*corrected_grades)
