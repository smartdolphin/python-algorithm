import unittest


def search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1
    return binary_search(data, start, end, target)


def binary_search(data, low, high, target):
    if low > high:
        return None

    mid = (low + high) // 2

    if target < data[mid]:
        return binary_search(data, low, mid - 1, target)
    elif data[mid] < target:
        return binary_search(data, mid + 1, high, target)
    else:
        return mid


class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(
            search([1, 2, 3, 4, 5], 4), 3
        )
        self.assertEqual(
            search([5, 4, 3, 2, 1], 4), 3
        )
        self.assertEqual(
            search([5, 4, 3, 2, 1], 5), 4
        )
        self.assertEqual(
            search([5, 4, 3, 2, 1], 1), 0
        )
        self.assertEqual(
            search([1, 2, 3, 4, 5], 6), None
        )
        self.assertEqual(
            search([5, 4, 3, 2, -1], 0), None
        )


if __name__ == '__main__':
    unittest.main()
