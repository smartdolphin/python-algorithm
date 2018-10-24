# 805. Split Array With Same Average
# https://leetcode.com/problems/split-array-with-same-average
import unittest


class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        target_sum = sum(A)
        if all([(i * target_sum) % len(A) != 0 for i in range(1, len(A)-1)]):
            return False
        A.sort()
        target_avg = target_sum / len(A)

        def dfs(cur_sum, size, start, memo):
            if (cur_sum, start) in memo:
                return False
            if size:
                memo.add((cur_sum, start))
                cur_avg = cur_sum / size
                if cur_avg == target_avg:
                    return True
                elif cur_avg > target_avg:
                    memo.add((cur_sum, start))
                    return False
                elif start >= len(A) or size >= len(A)-1:
                    memo.add((cur_sum, start))
                    return False
            for i in range(start+1, len(A)):
                if dfs(cur_sum + A[i], size + 1, i, memo):
                    return True
            return False
        return dfs(0, 0, 0, set())


class TestSplitArrayWithSameAvg(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(sol.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    unittest.TestCase()
