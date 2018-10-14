# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.count = 0
        self.result = 0

    # recursive
    # time: O(logN), space: O(logN)
    def kthSmallest_v0(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self._inorder_traversal(root, k)
        return self.result

    def _inorder_traversal(self, node, k):
        if node.left is not None:
            self._inorder_traversal(node.left, k)
        self.count += 1
        if k == self.count:
            self.result = node.val
            return
        if node.right is not None:
            self._inorder_traversal(node.right, k)

    # iterative
    # time: O(logN), space: O(1)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return 0


class TestKthSmallestBST(unittest.TestCase):
    def test(self):
        sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(4)
        self.assertEqual(
            sol.kthSmallest(root, 1),
            1
        )
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        self.assertEqual(
            sol.kthSmallest(root, 3),
            3
        )


if __name__ == '__main__':
    unittest.TestCase()
