# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses
import unittest


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    sum_hierarchy = 0
                    while stack[-1] != '(':
                        sum_hierarchy += stack.pop()
                    stack.pop()
                    stack.append(2 * sum_hierarchy)
        if len(stack) > 1:
            return sum(stack)
        return stack.pop()


class TestScoreParentheses(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(sol.scoreOfParentheses('()'), 1)
        self.assertEqual(sol.scoreOfParentheses('(())'), 2)
        self.assertEqual(sol.scoreOfParentheses('()()'), 2)
        self.assertEqual(sol.scoreOfParentheses('(()(()))'), 6)


if __name__ == '__main__':
    unittest.TestCase()
