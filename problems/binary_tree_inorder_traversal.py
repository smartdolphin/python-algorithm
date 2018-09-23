import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        self._helper(root, result)
        return result

    def _recursive_helper(self, node, result):
        if node.left is not None:
            self._recursive_helper(node.left, result)
        result.append(node.val)
        if node.right is not None:
            self._recursive_helper(node.right, result)


class TestInOrder(unittest.TestCase):
    def test(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        sol = Solution()
        self.assertEqual(
            sol.inorderTraversal(root),
            [1, 3, 2]
        )


if __name__ == '__main__':
    unittest.TestCase()
