import unittest


def quick_sort(arr):
    def _quick_sort(arr, first, last):
        if first < last:
            pivot = first
            i = first
            j = last

            while i < j:
                while arr[i] <= arr[pivot] and i < last:
                    i += 1
                while arr[j] > arr[pivot]:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[pivot], arr[j] = arr[j], arr[pivot]

            _quick_sort(arr, first, j - 1)
            _quick_sort(arr, j + 1, last)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


class TestQuickSort(unittest.TestCase):
    def test(self):
        arr = quick_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = quick_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = quick_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = quick_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = quick_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
