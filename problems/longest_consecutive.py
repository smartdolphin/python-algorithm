# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence
import unittest


class Solution:
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dic = set(nums)
        longest_num = 0

        for n in nums:
            if n - 1 not in num_dic:
                num_cnt = 1

                while n + 1 in num_dic:
                    num_cnt += 1
                    n += 1

                if num_cnt > longest_num:
                    longest_num = num_cnt
        return longest_num


class TestLongestConsecutive(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.longest_consecutive([100, 4, 200, 1, 3, 2]),
            4
        )


if __name__ == '__main__':
    unittest.TestCase()
