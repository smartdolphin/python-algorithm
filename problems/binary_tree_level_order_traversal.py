# 102. Binary tree level order traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [root]
        result = []

        while queue:
            result.append([node.val for node in queue])
            next_nodes = []
            for node in queue:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            queue = next_nodes
        return result


class TestLevelOrder(unittest.TestCase):
    def test(self):
        node = TreeNode(3)
        node.left = TreeNode(9)
        node.right = TreeNode(20)
        node.right.left = TreeNode(15)
        node.right.right = TreeNode(7)

        sol = Solution()
        self.assertEqual(
            sol.levelOrder(node),
            [[3], [9, 20], [15, 7]]
        )


if __name__ == '__main__':
    unittest.TestCase()
