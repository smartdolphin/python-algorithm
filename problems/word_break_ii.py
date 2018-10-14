# 140. Word Break II
# https://leetcode.com/problems/word-break-ii
import unittest


class Solution:
    def __init__(self):
        self.memo = {}

    def _word_break_helper(self, s, word_dic, start):
        if start in self.memo:
            return self.memo[start]
        res = []
        if start == len(s):
            res.append('')
        for end in range(start + 1, len(s) + 1):
            sub_str = s[start:end]
            if sub_str in word_dic:
                sub_rest = self._word_break_helper(s, word_dic, end)
                for sub in sub_rest:
                    sub = sub_str + (' ' if sub != '' else '') + sub
                    res.append(sub)
        self.memo[start] = res
        return res

    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        '''
        if not s:
            return []
        self.memo = {}
        result = self._word_break_helper(s, set(wordDict), 0)
        return result


class TestWordBreak(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']),
            [
              'cat sand dog',
              'cats and dog'
            ]
        )
        self.assertEqual(
            sol.wordBreak('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']),
            [
                'pine apple pen apple',
                'pine applepen apple',
                'pineapple pen apple',
            ]
        )
        self.assertEqual(
            sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
            []
        )


if __name__ == '__main__':
    unittest.TestCase()
