# 169. Majority Element
# https://leetcode.com/problems/majority-element
import unittest


class Solution:
    # time: O(n), space: O(1)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, cnt = 0, 0
        for n in nums:
            if cnt == 0:
                x = n
                cnt += 1
            elif x == n:
                cnt += 1
            else:
                cnt -= 1
        return x


class TestMajorityElement(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.majorityElement([3, 2, 3]), 3)
        self.assertEqual(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == '__main__':
    unittest.TestCase()
