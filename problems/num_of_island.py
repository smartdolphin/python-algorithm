# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands
import unittest


class Solution:
    def __init__(self):
        self.direction = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == '1' and grid[i][j] != 'v':
                    self.check_island(grid, i, j)
                    cnt += 1
        return cnt

    def is_neighborhood(self, grid, row, col):
        n_row = len(grid)
        n_col = len(grid[0])
        for r, c in self.direction:
            if (row + r >= 0 and
                row + r < n_row and
                col + c >= 0 and
                col + c < n_col and
                grid[row + r][col + c] == '1'):
                return True
        return False

    def check_island(self, grid, row, col):
        grid[row][col] = 'v'

        if not self.is_neighborhood(grid, row, col):
            return

        n_row = len(grid)
        n_col = len(grid[0])
        for r, c in self.direction:
            if (row + r >= 0 and
                row + r < n_row and
                col + c >= 0 and
                col + c < n_col and
                grid[row + r][col + c] == '1'):
                self.check_island(grid, row + r, col + c)


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
