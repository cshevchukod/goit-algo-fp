# task6.py - Завдання 6

def greedy_algorithm(items, budget):
    # список: (name, cost, calories, ratio)
    items_list = []
    for name, info in items.items():
        cost = info["cost"]
        cal = info["calories"]
        ratio = cal / cost
        items_list.append((name, cost, cal, ratio))

    # сортуємо за співвідношенням калорій до вартості (спадання)
    items_list.sort(key=lambda x: x[3], reverse=True)

    chosen = []
    total_cost = 0

    for name, cost, cal, ratio in items_list:
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost

    return chosen


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [0] * (budget + 1)

    keep = [[False] * (budget + 1) for _ in range(n)]

    for i in range(n):
        cost = items[names[i]]["cost"]
        cal = items[names[i]]["calories"]

        # йдемо назад, щоб кожну страву взяти максимум 1 раз
        for w in range(budget, cost - 1, -1):
            if dp[w - cost] + cal > dp[w]:
                dp[w] = dp[w - cost] + cal
                keep[i][w] = True

    # відновлення відповіді
    chosen = []
    w = budget
    for i in range(n - 1, -1, -1):
        if keep[i][w]:
            chosen.append(names[i])
            w -= items[names[i]]["cost"]

    chosen.reverse()
    return chosen


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    print("Budget:", budget)
    print("Greedy:", greedy_algorithm(items, budget))
    print("Dynamic programming:", dynamic_programming(items, budget))
