# 139. Word Break
# https://leetcode.com/problems/word-break
import unittest


class Solution:
    # brute force and memoization
    # time: O(n^2), space: O(n)
    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        '''
        size = len(s)
        word_set = set(wordDict)
        memo_dic = {}

        def dfs(s, start, memo_dic):
            if start == size:
                return True
            elif start in memo_dic:
                return memo_dic[start]
            else:
                for end in range(start + 1, size + 1):
                    sub = s[start:end]
                    if sub in word_set and dfs(s, end, memo_dic):
                        memo_dic[start] = True
                        return memo_dic[start]
                memo_dic[start] = False
                return memo_dic[start]
        return dfs(s, 0, memo_dic)

    # bfs
    # time: O(n^2), space: O(n)
    def wordBreak_v2(self, s, wordDict):
        size = len(s)
        word_set = set(wordDict)
        queue = [0]
        visit = [False] * size

        while queue:
            start = queue.pop()
            if not visit[start]:
                for end in range(start + 1, size + 1):
                    sub = s[start:end]
                    if sub in word_set:
                        queue.append(end)
                        if end == size:
                            return True
                visit[start] = True
        return False


class TestWordBreak(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(sol.wordBreak('leetcode', ['leet', 'code']))
        self.assertFalse(sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
        self.assertFalse(sol.wordBreak('aaaaaaa', ['aaaa', 'aa']))
        self.assertTrue(sol.wordBreak('bb', ['a', 'b', 'bbb', 'bbbb']))


if __name__ == '__main__':
    unittest.TestCase()
