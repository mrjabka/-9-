def can_all_fit(side, w, h, n):
    return (side // w) * (side // h) >= n


def find_minimum_side(w, h, n):
    left = min(w, h)
    right = max(w, h) * n
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_all_fit(mid, w, h, n):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


w, h, n = map(int, input().split())
print(find_minimum_side(w, h, n))
