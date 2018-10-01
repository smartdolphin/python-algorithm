# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands
import unittest


class Solution:
    def __init__(self):
        self.direction = ((0, -1), (-1, 0), (0, 1), (1, 0))
        self.n_row = None
        self.n_col = None

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        cnt = 0
        self.n_row = len(grid)
        self.n_col = len(grid[0])

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == '1':
                    self._check_island(grid, i, j)
                    cnt += 1
        return cnt

    def _check_island(self, grid, row, col):
        grid[row][col] = '0'

        for r, c in self.direction:
            if 0 <= row + r < self.n_row and \
               0 <= col + c < self.n_col and \
               grid[row + r][col + c] == '1':
                self._check_island(grid, row + r, col + c)


class TestNumOfIsland(unittest.TestCase):
    def test(self):
        sol = Solution()
        grid = [['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']]
        self.assertEqual(
            sol.numIslands(grid),
            1
        )
        grid = [['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']]
        self.assertEqual(
            sol.numIslands(grid),
            3
        )


if __name__ == '__main__':
    unittest.TestCase()
