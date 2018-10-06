# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
import unittest


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1:
            return s

        arr = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = size - 1

        while left < right:
            if arr[left] not in vowels:
                left += 1
            if arr[right] not in vowels:
                right -= 1
            if arr[left] in vowels and arr[right] in vowels:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return ''.join(arr)


class TestReverseVowels(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.reverseVowels('aA'),
            'Aa'
        )
        self.assertEqual(
            sol.reverseVowels('hello'),
            'holle'
        )
        self.assertEqual(
            sol.reverseVowels('leetcode'),
            'leotcede'
        )


if __name__ == '__main__':
    unittest.TestCase()
