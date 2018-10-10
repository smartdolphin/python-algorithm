# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix
import unittest


class Solution:
    # if col=3, row=3, then 3→, 2↓, 2←, 1↑, 1→
    # if col=4, row=2, then 4→, 2↓, 3←, 1↑, 2→
    # if col=4, row=4, then 4→, 3↓, 3←, 2↑, 2→, 1↓, 1←
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        n_row = len(matrix)
        n_col = len(matrix[0])
        result = []
        col, row = -1, 0
        interval = 1
        while n_col > 0 and n_row > 0:
            for _ in range(n_col):
                col += interval
                result.append(matrix[row][col])
            n_row -= 1
            n_col -= 1
            for _ in range(n_row):
                row += interval
                result.append(matrix[row][col])
            interval *= -1
        return result


class TestSpiralMatrix(unittest.TestCase):
    def test(self):
        sol = Solution()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(
            sol.spiralOrder(matrix),
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        )
        matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]
        ]
        self.assertEqual(
            sol.spiralOrder(matrix),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )


if __name__ == '__main__':
    unittest.TestCase()
