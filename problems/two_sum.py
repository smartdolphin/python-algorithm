# 1. Two Sum
# https://leetcode.com/problems/two-sum
import unittest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        raise Exception('No solution')


class TestTwoSum(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.twoSum([2, 7, 11, 15], 9),
            [0, 1]
        )
        self.assertEqual(
            solution.twoSum([1, 2, 3, 9], 10),
            [0, 3]
        )


if __name__ == '__main__':
    unittest.TestCase()
