# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses
import unittest


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in brackets_dic:
                if stack and stack[-1] == brackets_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


class TestValidParentheses(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertTrue(sol.isValid('()'))
        self.assertTrue(sol.isValid('[{}]'))
        self.assertTrue(sol.isValid('[]{}()'))
        self.assertFalse(sol.isValid('[)'))
        self.assertFalse(sol.isValid('([)]'))


if __name__ == '__main__':
    unittest.TestCase()
