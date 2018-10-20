# 283. Move Zeros
# https://leetcode.com/problems/move-zeroes
import unittest


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        size = len(nums)
        none_zero_idx, cur = 0, 0
        while cur < size:
            if nums[cur] != 0:
                nums[none_zero_idx], nums[cur] = nums[cur], nums[none_zero_idx]
                none_zero_idx += 1
            cur += 1


class TestMoveZeros(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.moveZeroes([0, 1, 0, 3, 12]),
            [1, 3, 12, 0, 0]
        )


if __name__ == '__main__':
    unittest.TestCase()
