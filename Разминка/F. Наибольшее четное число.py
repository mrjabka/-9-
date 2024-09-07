def form_largest_even_number(d1, d2, d3):
    digits = [d1, d2, d3]
    max_number = -1

    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            for k in range(3):
                if k == i or k == j:
                    continue

                number = digits[i] * 100 + digits[j] * 10 + digits[k]

                if number % 2 == 0 and number > max_number:
                    max_number = number

    return max_number
