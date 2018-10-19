# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix
import unittest


class Solution:
    def longestCommonPrefix(self, strs):
        '''
        :type strs: List[str]
        :rtype: str
        '''
        if not strs:
            return ''
        min_size = min([len(s) for s in strs])
        longest_len = 0
        for idx in range(min_size):
            is_same = True
            for i, s in enumerate(strs):
                if i == 0:
                    first = s[idx]
                else:
                    if s[idx] != first:
                        is_same = False
            if is_same:
                longest_len += 1
            else:
                break
        return strs[0][:longest_len]


class TestEncodeDecodeString(unittest.TestCase):
    def test(self):
        # Your Codec object will be instantiated and called as such:
        sol = Solution()
        self.assertEqual(
            sol.longestCommonPrefix(['flower', 'flow', 'flight']),
            'fl'
        )
        self.assertEqual(
            sol.longestCommonPrefix(['dog', 'racecar', 'car']),
            ''
        )


if __name__ == '__main__':
    unittest.TestCase()
