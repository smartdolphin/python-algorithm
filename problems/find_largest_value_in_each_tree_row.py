# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            result.append(max([node.val for node in queue]))
            next_nodes = []
            for node in queue:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            queue = next_nodes
        return result


class TestFindLargestValue(unittest.TestCase):
    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.right.right = TreeNode(9)
        sol = Solution()
        self.assertEqual(
            sol.largestValues(root),
            [1, 3, 9]
        )


if __name__ == '__main__':
    unittest.TestCase()
