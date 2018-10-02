import unittest


def counting_sort(arr):
    def _counting_sort(list, smallest, largest):
        n_bins = largest - smallest + 1
        bins = [0] * n_bins
        for i in list:
            bins[i - smallest] += 1
        return [i + smallest for i, n in enumerate(bins) for _ in range(n)]

    result = _counting_sort(arr, min(arr), max(arr))
    return result


class TestCountingSort(unittest.TestCase):
    def test(self):
        arr = counting_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = counting_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = counting_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = counting_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = counting_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
