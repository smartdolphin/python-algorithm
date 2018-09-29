import unittest


def bubble_sort(arr):
    for size in reversed(range(len(arr))):
        for i in range(size):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    return arr


class TestBubbleSort(unittest.TestCase):
    def test(self):
        arr = bubble_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = bubble_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = bubble_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = bubble_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = bubble_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
