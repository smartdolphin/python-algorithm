# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses
import unittest


class Solution:
    # brute force
    # time: O(n*2^2n), space: O(2n)
    def generate_parentheses(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def dfs(s, size):
            if size == n * 2:
                if self.is_valid(s):
                    result.append(s)
                return
            for c in ['(', ')']:
                dfs(s + c, size + 1)

        dfs('(', 1)
        return result

    def is_valid(self, s):
        cnt = 0
        for c in s:
            cnt += 1 if c == '(' else -1
            if cnt < 0:
                return False
        return cnt == 0

    # back tracking
    # time: O(4^n/sqrt(n)), space: O(2n)
    def generate_parentheses_v2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(s='', left=0, right=0):
            if len(s) == n * 2:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return result


class TestGenerateParentheses(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.generateParenthesis(3),
            [
                '((()))',
                '(()())',
                '(())()',
                '()(())',
                '()()()'
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
