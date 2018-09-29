import unittest


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


class TestSelectionSort(unittest.TestCase):
    def test(self):
        arr = selection_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = selection_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = selection_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = selection_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = selection_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
