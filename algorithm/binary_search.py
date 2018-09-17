import unittest


def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        self.assertNotEqual(
            binary_search(4, [1, 2, 3, 4, 5]), None
        )
        self.assertNotEqual(
            binary_search(4, [5, 4, 3, 2, 1]), None
        )
        self.assertEqual(
            binary_search(6, [1, 2, 3, 4, 5]), None
        )
        self.assertEqual(
            binary_search(0, [5, 4, 3, 2, -1]), None
        )


if __name__ == '__main__':
    unittest.main()
