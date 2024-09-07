numbers = input().split()
reversed_numbers = [str(int(num[::-1])) for num in numbers]
output_string = ' '.join(reversed(reversed_numbers))
print(output_string)
