# task7.py - Завдання 7

import random

def monte_carlo_dice(trials):
    counts = {s: 0 for s in range(2, 13)}

    for _ in range(trials):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        s = d1 + d2
        counts[s] += 1

    probs = {s: counts[s] / trials for s in counts}
    return counts, probs


def print_table(counts, probs, trials):
    print("Кількість симуляцій:", trials)
    print("Сума | К-ть | Ймовірність")
    print("-------------------------")
    for s in range(2, 13):
        p = probs[s] * 100
        print(f"{s:>4} | {counts[s]:>4} | {p:>9.2f}%")


if __name__ == "__main__":
    trials = 100000  # "велика кількість" кидків
    counts, probs = monte_carlo_dice(trials)
    print_table(counts, probs, trials)
