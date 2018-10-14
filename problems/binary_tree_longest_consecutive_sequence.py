# 298. Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, parent, length):
            if node is None:
                return length
            length = length + 1 if parent is not None and parent.val + 1 == node.val else 1
            return max(length, max(dfs(node.left, node, length),
                                   dfs(node.right, node, length)))
        return dfs(root, None, 0)


class TestBinaryTreeLongestConsecutiveSeq(unittest.TestCase):
    def test(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)
        sol = Solution()
        self.assertEqual(sol.longestConsecutive(root), 3)
        root = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(1)
        self.assertEqual(sol.longestConsecutive(root), 2)


if __name__ == '__main__':
    unittest.TestCase()
