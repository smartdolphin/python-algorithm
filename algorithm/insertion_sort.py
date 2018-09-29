import unittest


def insertion_sort(arr):
    for size in range(1, len(arr)):
        val = arr[size]
        i = size
        while i > 0 and arr[i - 1] > val:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = val
    return arr


class TestInsertionSort(unittest.TestCase):
    def test(self):
        arr = insertion_sort([6, 5, 3, 1, 8, 7, 2, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5, 6, 7, 8]
        )
        arr = insertion_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = insertion_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = insertion_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = insertion_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = insertion_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
