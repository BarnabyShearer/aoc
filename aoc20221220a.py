class Node:
    def __init__(self, data, length):
        self.data = data
        self.next = None
        self.prev = None
        self.orig = None
        self.length = length

    def __repr__(self):
        return str(self.data)

    def mv(self, off):
        if off == 0:
            return
        node = self
        self.prev.next = self.next
        self.next.prev = self.prev

        for _ in range(off % (self.length - 1)):
            node = node.next

        self.next = node.next
        self.next.prev = self
        self.prev = node
        node.next = self


class LinkedList:
    def __init__(self, nodes):
        length = len(nodes)
        node = Node(nodes.pop(0), length)
        self.head = node
        for elem in nodes:
            node.next = Node(elem, length)
            node.orig = node.next
            node.next.prev = node
            node = node.next
        node.next = self.head
        self.head.prev = node


def parse(data, key):
    return [int(x) * key for x in data.split("\n")]


def aoc(data, key=1, num=1):
    data = parse(data, key)
    ll = LinkedList(data)

    for _ in range(num):
        node = ll.head
        while node:
            node.mv(node.data)
            node = node.orig

    node = ll.head
    while node.data != 0:
        node = node.next

    total = 0
    for _ in range(3):
        for _ in range(1000):
            node = node.next
        total += node.data
    return total
