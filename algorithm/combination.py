import unittest


class Solution:
    def __init__(self):
        self.stack = []

    def combination(self, arr, offset, length, k, result):
        if k == 0:
            result.append([''.join(self.stack[:])])
            return
        for i in range(offset, length):
            self.stack.append(arr[i])
            self.combination(arr, i, length, k - 1, result)
            self.stack.pop()


class TestCombination(unittest.TestCase):
    def test(self):
        sol = Solution()
        arr = ['A', 'B', 'C']
        result = []
        sol.combination(arr, 0, len(arr), 2, result)
        self.assertEqual(
            result,
            [
                ['AA'],
                ['AB'],
                ['AC'],
                ['BB'],
                ['BC'],
                ['CC'],
            ]
        )
        result = []
        sol.combination(arr, 0, len(arr), 3, result)
        self.assertEqual(
            result,
            [
                ['AAA'],
                ['AAB'],
                ['AAC'],
                ['ABB'],
                ['ABC'],
                ['ACC'],
                ['BBB'],
                ['BBC'],
                ['BCC'],
                ['CCC'],
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
