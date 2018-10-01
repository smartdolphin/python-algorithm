# 155. Min Stack
# https://leetcode.com/problems/min-stack
import unittest


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min > x:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.stack.pop():
            self.min = float('inf')
            for i in self.stack:
                if self.min > i:
                    self.min = i

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


class TestNumOfIsland(unittest.TestCase):
    def test(self):
        # Your MinStack object will be instantiated and called as such:
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(
            min_stack.getMin(),
            -3
        )
        min_stack.pop()
        self.assertEqual(
            min_stack.top(),
            0
        )
        self.assertEqual(
            min_stack.getMin(),
            -2
        )


if __name__ == '__main__':
    unittest.TestCase()
