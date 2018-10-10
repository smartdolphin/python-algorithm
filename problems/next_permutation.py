# 31. Next Permutation
# https://leetcode.com/problems/next-permutation
import unittest


class Solution:
    # 123 -> 132
    # 231 -> 312
    # time: O(n), space: O(1)
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        a = size - 2
        while a >= 0 and nums[a] >= nums[a + 1]:
            a -= 1
        if a >= 0:
            b = size - 1
            while b >= 0 and nums[a] >= nums[b]:
                b -= 1
            nums[a], nums[b] = nums[b], nums[a]
        start = a + 1
        end = size - 1
        # ascend order
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


class TestNextPermutation(unittest.TestCase):
    def test(self):
        sol = Solution()
        nums = [1, 2, 3]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])
        nums = [3, 2, 1]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])
        nums = [1, 1, 5]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])
        nums = [2, 3, 1]
        sol.nextPermutation(nums)
        self.assertEqual(nums, [3, 1, 2])


if __name__ == '__main__':
    unittest.TestCase()
