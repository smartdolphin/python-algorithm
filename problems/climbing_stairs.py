import unittest


class Solution:
    # 1 2 3 5 8 -> like fibonacci

    # if n=5
    # 1 1 1 1
    # 1 1 2
    # 2 1 1
    # 1 2 1
    # 2 2

    # dynamic programming
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        ans = [0] * n
        ans[0] = 1
        ans[1] = 2
        ans[2] = 3
        for i in range(3, n):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[-1]

    # dfs version
    def climb_stairs_v0(self, n):
        def dfs(n):
            if n <= 2:
                return n
            return dfs(n - 2) + dfs(n - 1)

        return dfs(n)


class TestClimbingStair(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.climb_stairs(0), 0)
        self.assertEqual(sol.climb_stairs(1), 1)
        self.assertEqual(sol.climb_stairs(2), 2)
        self.assertEqual(sol.climb_stairs(3), 3)
        self.assertEqual(sol.climb_stairs(4), 5)
        self.assertEqual(sol.climb_stairs(5), 8)


if __name__ == '__main__':
    unittest.TestCase()