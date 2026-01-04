# task1.py - Завдання 1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 1) Реверсування списку
    def reverse(self):
        prev = None
        cur = self.head

        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        self.head = prev

    # 2) Сортування вставками
    def insertion_sort(self):
        sorted_head = None
        cur = self.head

        while cur is not None:
            nxt = cur.next
            cur.next = None  # від'єднали вузол

            sorted_head = self._sorted_insert(sorted_head, cur)
            cur = nxt

        self.head = sorted_head

    # Допоміжна функція для insertion sort:
    def _sorted_insert(self, sorted_head, node):
        if sorted_head is None or node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        cur = sorted_head
        while cur.next is not None and cur.next.data < node.data:
            cur = cur.next

        node.next = cur.next
        cur.next = node
        return sorted_head

    # 3) Злиття двох відсортованих списків
    def merge_sorted_with(self, other):
        a = self.head
        b = other.head

        merged = LinkedList()

        if a is None:
            merged.head = b
            return merged
        if b is None:
            merged.head = a
            return merged

        if a.data <= b.data:
            merged.head = a
            a = a.next
        else:
            merged.head = b
            b = b.next

        tail = merged.head  # хвіст нового списку

        while a is not None and b is not None:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a is not None else b
        return merged


if __name__ == "__main__":

    l1 = LinkedList()
    for x in [4, 2, 5, 1, 3]:
        l1.insert_at_end(x)

    print("Початковий список:")
    l1.print_list()

    l1.reverse()
    print("\nПісля реверсу:")
    l1.print_list()

    l1.insertion_sort()
    print("\nПісля сортування вставками:")
    l1.print_list()

    a = LinkedList()
    for x in [1, 3, 5, 7]:
        a.insert_at_end(x)

    b = LinkedList()
    for x in [2, 4, 6, 8]:
        b.insert_at_end(x)

    merged = a.merge_sorted_with(b)
    print("\nЗлиття двох відсортованих списків:")
    merged.print_list()
