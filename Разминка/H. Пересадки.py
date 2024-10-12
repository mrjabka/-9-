def count_common_stops(a1, b1, a2, b2):
    # Определяем диапазон остановок для каждого автобуса
    range1 = set(range(min(a1, b1), max(a1, b1) + 1))
    range2 = set(range(min(a2, b2), max(a2, b2) + 1))

    common_stops = range1.intersection(range2)

    return len(common_stops)


a1, b1, a2, b2 = map(int, input().split())

print(count_common_stops(a1, b1, a2, b2))
