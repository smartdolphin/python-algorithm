# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle
import unittest


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result.append([1])

        for depth in range(1, numRows):
            temp = []
            for i in range(depth + 1):
                if i == 0:
                    temp.append(1)
                elif i == depth:
                    temp.append(1)
                else:
                    temp.append(result[depth - 1][i - 1] + result[depth - 1][i])
            result.append(temp)
        return result


class TestGenerate(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.generate(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
