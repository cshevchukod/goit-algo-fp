# task3.py - Завдання 3

import heapq


def dijkstra(graph, start):
    # початкові відстані
    distances = {}
    for v in graph:
        distances[v] = float("inf")
    distances[start] = 0

    # бінарна купа (піраміда)
    heap = [(0, start)]

    while heap:
        current_dist, v = heapq.heappop(heap)

        if current_dist > distances[v]:
            continue

        for to, weight in graph[v]:
            new_dist = current_dist + weight
            if new_dist < distances[to]:
                distances[to] = new_dist
                heapq.heappush(heap, (new_dist, to))

    return distances


if __name__ == "__main__":

    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }

    start = "A"
    result = dijkstra(graph, start)

    print(f"Найкоротші відстані від {start}:")
    for v in result:
        print(v, "->", result[v])
