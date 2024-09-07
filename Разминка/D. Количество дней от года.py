def days_from_start_of_2010(day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(days_in_month[:month-1]) + day
    return days

day, month = map(int, input().split())
print(days_from_start_of_2010(day, month))
