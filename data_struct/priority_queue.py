import unittest


class PriorityQueue(object):
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.heap_size = 0
        self.heap = []
        for i in range(self.max_size):
            self.heap.append(0)

    def is_empty(self):
        return self.heap_size == 0

    def push(self, value):
        # is full
        if self.heap_size + 1 > self.max_size:
            return
        self.heap[self.heap_size] = value

        pos = self.heap_size
        while pos > 0 and self.heap[pos] < self.heap[(pos - 1) // 2]:
            parent = (pos - 1) // 2
            self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
            pos = parent
        self.heap_size += 1

    def pop(self):
        if self.heap_size <= 0:
            return None

        value = self.heap[0]
        self.heap_size -= 1
        self.heap[0] = self.heap[self.heap_size]

        pos = 0
        while pos < self.heap_size and pos * 2 + 1 < self.heap_size:
            if pos * 2 + 2 >= self.heap_size:
                child = pos * 2 + 1
            else:
                if self.heap[pos * 2 + 1] < self.heap[pos * 2 + 2]:
                    child = pos * 2 + 1
                else:
                    child = pos * 2 + 2
            if self.heap[pos] < self.heap[child]:
                break

            self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
            pos = child
        return value


class TestPriorityQueue(unittest.TestCase):
    def test(self):
        pq = PriorityQueue()
        pq.push(10)
        pq.push(49)
        pq.push(38)
        pq.push(17)
        pq.push(56)
        pq.push(92)
        pq.push(8)
        pq.push(1)
        pq.push(13)
        pq.push(55)

        result = []
        while not pq.is_empty():
            result.append(pq.pop())
        self.assertEqual(
            result,
            [1, 8, 10, 13, 17, 38, 49, 55, 56, 92]
        )


if __name__ == '__main__':
    unittest.TestCase()
