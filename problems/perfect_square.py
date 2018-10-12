# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares
import unittest


class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        queue, depth = {n}, 1
        while queue:
            next_nodes = set()
            for val in queue:
                for sq in squares:
                    if val == sq:
                        return depth
                    elif val < sq:
                        break
                    next_nodes.add(val - sq)
            queue = next_nodes
            depth += 1
        return depth


class TestPerfectSquares(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.numSquares(12), 3)
        self.assertEqual(sol.numSquares(13), 2)


if __name__ == '__main__':
    unittest.TestCase()
