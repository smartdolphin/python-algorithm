# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii
import unittest


class Solution:
    # brute force
    # time: O(n*m), space: O(1)
    def searchMatrix_v0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row:
                return True
        return False

    # divide & conquer
    # time: O(2n*logn), space: O(logN)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        def search_helper(left, up, right, down):
            if left > right or up > down:
                return False
            if target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search_helper(left, row, mid - 1, down) or\
                   search_helper(mid + 1, up, right, row - 1)
        return search_helper(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


class TestSearchMatrix(unittest.TestCase):
    def test(self):
        sol = Solution()
        matrix = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertTrue(sol.searchMatrix(matrix, 9))
        self.assertTrue(sol.searchMatrix(matrix, 1))
        self.assertTrue(sol.searchMatrix(matrix, 18))
        self.assertTrue(sol.searchMatrix(matrix, 30))


if __name__ == '__main__':
    unittest.TestCase()
