# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator
import unittest


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._travel_left(root)

    def _travel_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self._travel_left(node.right)
        return node.val


class TestBSTIterator(unittest.TestCase):
    def test(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(0)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)

        # Your BSTIterator will be called like this:
        i, v = BSTIterator(root), []
        while i.hasNext():
            v.append(i.next())
        self.assertEqual(
            v, [0, 1, 2, 3, 4, 5, 6, 7, 8]
        )


if __name__ == '__main__':
    unittest.TestCase()
