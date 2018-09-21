import unittest


class Stack(object):
    def __init__(self):
        self.stack = []

    def clear(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


class TestStack(unittest.TestCase):
    def test(self):
        data_set = [1, 2, 3, 4, 5]
        stack = Stack()
        stack.clear()

        for data in data_set:
            stack.push(data)

        result = []
        while not stack.is_empty():
            value = stack.pop()
            if value is not None:
                result.append(value)

        self.assertEqual(
            result, [5, 4, 3, 2, 1]
        )


if __name__ == '__main__':
    unittest.TestCase()
