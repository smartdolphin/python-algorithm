# 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree
import unittest


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0
            elif root.children == []:
                return 1
            return max([dfs(c) for c in root.children]) + 1
        return dfs(root)


class TestRobotToOrigin(unittest.TestCase):
    def test(self):
        sol = Solution()
        node = Node(1)
        node.children = [Node(3), Node(2), Node(4)]
        node.children[0].children = [Node(5), Node(6)]
        self.assertTrue(
            sol.maxDepth(node),
            3
        )


if __name__ == '__main__':
    unittest.TestCase()
