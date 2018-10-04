# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator
import unittest


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s.isdigit():
            return int(s)

        postfix_expr = self.parser(s)
        return self.calculator(postfix_expr)

    def parser(self, s):
        op_weight = {
            '/': 2,
            '*': 2,
            '+': 1,
            '-': 1,
            '(': 0,
        }
        output = []
        stack = []
        digit_str = ''

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                digit_str += c
            else:
                if digit_str:
                    output.append(digit_str)
                    digit_str = ''

                # operand
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    while stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()
                else:
                    while stack != [] and op_weight[stack[-1]] >= op_weight[c]:
                        output.append(stack.pop())
                    stack.append(c)
        if digit_str:
            output.append(digit_str)
        while stack:
            output.append(stack.pop())
        return output

    def calculator(self, postfix_expr):
        calculate_func = {
            '*' : lambda l, r: l * r,
            '/' : lambda l, r: l / r,
            '+' : lambda l, r: l + r,
            '-' : lambda l, r: l - r,
        }
        stack = []
        for c in postfix_expr:
            if c.isdigit():
                stack.append(c)
            else:
                right_val = int(stack.pop())
                left_val = int(stack.pop())
                stack.append(calculate_func[c](left_val, right_val))
        return int(stack.pop())


class TestPow(unittest.TestCase):
    def test(self):
        sol = Solution()
        self.assertEqual(
            sol.calculate('1 + 1'),
            2
        )
        self.assertEqual(
            sol.calculate(' 2-1 + 2 '),
            3
        )
        self.assertEqual(
            sol.calculate('2147483647'),
            2147483647
        )
        self.assertEqual(
            sol.calculate(' 123'),
            123
        )
        self.assertEqual(
            sol.calculate('1-11'),
            -10
        )
        self.assertEqual(
            sol.calculate('0-2147483647'),
            -2147483647
        )


if __name__ == '__main__':
    unittest.TestCase()
