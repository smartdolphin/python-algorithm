# 421. Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array
import unittest


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, mask = 0, 0
        for i in range(31, -1, -1):
            possible_max = maximum | 1 << i
            mask = mask | 1 << i
            bits = set()
            for n in nums:
                bits.add(n & mask)
            for bit in bits:
                if bit ^ possible_max in bits:
                    maximum = possible_max
                    break
        return maximum


class TestFindMaximumXor(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.findMaximumXOR([3, 10, 5, 25, 2, 8]),
            28
        )


if __name__ == '__main__':
    unittest.TestCase()
