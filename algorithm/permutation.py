import unittest


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def permutation(arr, length, offset, result):
    if offset == length:
        result.append(arr[:])
        return
    for i in range(offset, length):
        swap(arr, i, offset)
        permutation(arr, length, offset + 1, result)
        swap(arr, i, offset)


class TestPermutation(unittest.TestCase):
    def test(self):
        arr = ['A', 'B', 'C']
        result = []
        permutation(arr, len(arr), 0, result)
        self.assertEqual(
            result,
            [
                ['A', 'B', 'C'],
                ['A', 'C', 'B'],
                ['B', 'A', 'C'],
                ['B', 'C', 'A'],
                ['C', 'B', 'A'],
                ['C', 'A', 'B']
            ]
        )
        arr = ['1', '2', '3']
        result = []
        permutation(arr, len(arr), 0, result)
        self.assertEqual(
            result,
            [
                ['1', '2', '3'],
                ['1', '3', '2'],
                ['2', '1', '3'],
                ['2', '3', '1'],
                ['3', '2', '1'],
                ['3', '1', '2']
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
