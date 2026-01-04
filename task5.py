# task5.py - Завдання 5

import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / (2 ** layer)
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / (2 ** layer)
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.clf()
    if title:
        plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)


def build_heap_tree(heap_array):
    # Побудувати бінарне дерево з масиву купи (left=2*i+1, right=2*i+2)
    if not heap_array:
        return None

    nodes = [Node(value) for value in heap_array]

    for i in range(len(nodes)):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            nodes[i].left = nodes[li]
        if ri < len(nodes):
            nodes[i].right = nodes[ri]

    return nodes[0]


def get_nodes_bfs(root):
    # Зібрати всі вузли (BFS), щоб знати скільки їх (для кольорів)
    if root is None:
        return []

    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result


def step_color(i, n):
    # Колір від темного до світлого (#RRGGBB)
    if n <= 1:
        return "#C0E6FF"

    start = 30   # темніше
    end = 200    # світліше
    x = start + (end - start) * i // (n - 1)

    # робимо відтінок синього: (x, x, 255) - простий градієнт
    return f"#{x:02X}{x:02X}FF"


def reset_colors(nodes):
    for node in nodes:
        node.color = "skyblue"


def visualize_dfs(root):
    # DFS (стек) + покрокова візуалізація
    nodes_all = get_nodes_bfs(root)
    reset_colors(nodes_all)

    stack = [root]  # стек
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        # щоб лівий був перший, правий додаємо раніше
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    plt.figure(figsize=(8, 5))
    plt.ion()

    n = len(order)
    for i, node in enumerate(order):
        node.color = step_color(i, n)
        draw_tree(root, f"DFS крок {i + 1}/{n}")
        plt.pause(0.8)

    plt.ioff()
    plt.show()


def visualize_bfs(root):
    # BFS (черга) + покрокова візуалізація
    nodes_all = get_nodes_bfs(root)
    reset_colors(nodes_all)

    q = deque([root])  # черга
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    plt.figure(figsize=(8, 5))
    plt.ion()

    n = len(order)
    for i, node in enumerate(order):
        node.color = step_color(i, n)
        draw_tree(root, f"BFS крок {i + 1}/{n}")
        plt.pause(0.8)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    # дерево так само, як у Завданні 4 (з масиву купи)
    heap = [0, 4, 1, 5, 10, 3]
    root = build_heap_tree(heap)

    visualize_dfs(root)
    visualize_bfs(root)
