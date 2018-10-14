# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # time: O(n), space: O(n)
    def isSymmetric_v0(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.is_compare(root.left, root.right):
            return True
        return False

    def is_compare(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return self.is_compare(a.right, b.left) and self.is_compare(a.left, b.right)

    # iterative
    # time: O(n), space: O(1)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root, root]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True


class TestSymmetricTree(unittest.TestCase):
    def test(self):
        sol = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(sol.isSymmetric(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertFalse(sol.isSymmetric(root))


if __name__ == '__main__':
    unittest.TestCase()
