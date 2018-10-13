# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element
import unittest


class Solution:
    # linear solution
    # time: O(n), space: O(1)
    def findPeakElement_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return 0

        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                return i
        return size - 1

    # binary search recursive
    # time: O(logN), space: O(logN)
    def findPeakElement_v1(self, nums):
        def binary_search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                return binary_search(mid + 1, right)
            elif nums[mid] > nums[mid + 1]:
                return binary_search(left, mid)
            else:
                return mid
        return binary_search(0, len(nums) - 1)

    # binary search iterative
    # time: O(logN), space: O(1)
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
        return left


class TestFindPeakElement(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.findPeakElement([1, 2, 3, 1]), 2)
        self.assertEqual(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]), 5)
        self.assertEqual(sol.findPeakElement([1, 2, 3, 1]), 2)


if __name__ == '__main__':
    unittest.TestCase()
