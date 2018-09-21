import unittest


class Queue(object):
    def __init__(self):
        self.queue = []

    def clear(self):
        self.queue.clear()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)


class TestQueue(unittest.TestCase):
    def test(self):
        data_set = [1, 2, 3, 4, 5]
        queue = Queue()
        queue.clear()

        for data in data_set:
            queue.enqueue(data)

        result = []
        while not queue.is_empty():
            value = queue.dequeue()
            if value is not None:
                result.append(value)

        self.assertEqual(
            result, [1, 2, 3, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
