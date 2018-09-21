import unittest


class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(item)

    def remove(self, item):
        if self.head.value == item:
            self.head = self.head.next
        else:
            current = self.head
            while current is not None:
                if current.value == item:
                    self.remove_item(item)
                    return
                current = current.next
            print('item does not exist')

    def remove_item(self, item):
        prev = None
        current = self.head
        while current is not None:
            if current.value == item:
                next_node = current.next
                prev.next = next_node
                break
            prev = current
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def __call__(self):
        self.print_list()


class LinkedListTest(unittest.TestCase):
    def test(self):
        list = LinkedList(1)
        self.assertEqual(list.head.value, 1)
        list.add(2)
        self.assertEqual(list.head.next.value, 2)
        list.add(3)
        self.assertEqual(list.head.next.next.value, 3)
        list.remove(1)
        self.assertEqual(list.head.value, 2)
        list.remove(2)
        self.assertEqual(list.head.value, 3)
        list.add(4)
        self.assertEqual(list.head.next.value, 4)
        list.add(5)
        self.assertEqual(list.head.next.next.value, 5)
        list.remove(5)
        self.assertEqual(list.head.next.next, None)
        list.remove(3)
        self.assertEqual(list.head.next, None)
        list.remove(4)
        self.assertEqual(list.head, None)


if __name__ == '__main__':
    unittest.TestCase()
