def find_first_and_last_occurrence(sorted_list, query):
    left, right = 0, len(sorted_list) - 1
    first_occurrence, last_occurrence = -1, -1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < query:
            left = mid + 1
        elif sorted_list[mid] > query:
            right = mid - 1
        else:
            first_occurrence = mid
            right = mid - 1

    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < query:
            left = mid + 1
        elif sorted_list[mid] > query:
            right = mid - 1
        else:
            last_occurrence = mid
            left = mid + 1

    if first_occurrence == -1:
        return 0
    else:
        return first_occurrence + 1, last_occurrence + 1


n, m = map(int, input().split())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

for query in second_list:
    result = find_first_and_last_occurrence(first_list, query)
    if result == 0:
        print(0)
    else:
        print(result[0], result[1])
