# task7.py - Завдання 7

import random

def monte_carlo(trials):
    counts = {s: 0 for s in range(2, 13)}

    for _ in range(trials):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1

    probs = {s: counts[s] / trials for s in counts}
    return counts, probs


def print_table(counts, probs):
    print("Сума | Ймовірність")
    print("------------------")
    for s in range(2, 13):
        print(f"{s:>4} | {probs[s] * 100:>9.2f}%")


if __name__ == "__main__":
    trials = 100000
    counts, probs = monte_carlo(trials)

    print("Кількість кидків:", trials)
    print_table(counts, probs)
