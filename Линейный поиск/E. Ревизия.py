def find_two_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("Incorrect input")

    smallest = float('inf')
    second_smallest = float('inf')

    for number in numbers:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    return second_smallest, smallest


N = int(input())
droid_numbers = list(map(int, input().split()))

result = find_two_smallest(droid_numbers)

print(result[1], result[0])
