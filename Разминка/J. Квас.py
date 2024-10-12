def find_optimal_city(N, demands):
    min_cost = float('inf')
    best_city = 0

    for city in range(N):
        cost = 0

        for i in range(N):
            distance = min(abs(city - i), N - abs(city - i))
            cost += demands[i] * distance

        if cost < min_cost:
            min_cost = cost
            best_city = city + 1  # город считая от 1

    return best_city


# Чтение ввода
input_data = input().strip().split()
N = int(input_data[0])
demands = list(map(int, input_data[1:]))

# Поиск оптимального города
optimal_city = find_optimal_city(N, demands)
print(optimal_city)
