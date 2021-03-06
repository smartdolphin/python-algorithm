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
        stack = []
        result = []
        curr = root

        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


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
