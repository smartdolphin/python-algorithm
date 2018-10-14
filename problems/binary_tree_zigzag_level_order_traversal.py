# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursive
    # time: O(n), space: O(n)
    def zigzagLevelOrder_v0(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = {}
        self._traversal(root, 0)
        return [values for values in self.result.values()]

    def _traversal(self, node, depth):
        if node is None:
            return
        if depth not in self.result:
            self.result[depth] = [node.val]
        else:
            if depth % 2 == 1:
                # reversed
                if depth in self.result:
                    self.result[depth].insert(0, node.val)
            else:
                if depth in self.result:
                    self.result[depth].append(node.val)
        if node.left is not None:
            self._traversal(node.left, depth + 1)
        if node.right is not None:
            self._traversal(node.right, depth + 1)

    # iterative using queue
    # time: O(n), space: O(1)
    def zigzagLevelOrder_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = {}
        depth = 0
        while queue:
            if depth not in result:
                result[depth] = []
            next_nodes = []
            while queue:
                node = queue.pop(0)
                if depth % 2 == 1:
                    result[depth].insert(0, node.val)
                else:
                    result[depth].append(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            queue = next_nodes
            depth += 1
        return [values for values in result.values()]

    # iterative using stack
    # time: O(n), space: O(1)
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        result = []
        is_reverse = False
        while stack:
            next_nodes = []
            level_list = []
            while stack:
                node = stack.pop()
                level_list.append(node.val)
                if is_reverse:
                    if node.right is not None:
                        next_nodes.append(node.right)
                    if node.left is not None:
                        next_nodes.append(node.left)
                else:
                    if node.left is not None:
                        next_nodes.append(node.left)
                    if node.right is not None:
                        next_nodes.append(node.right)
            result.append(level_list)
            stack = next_nodes
            is_reverse = False if is_reverse else True
        return result


class TestBinaryTreeZigzagLevelOrderTraversal(unittest.TestCase):
    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        sol = Solution()
        self.assertEqual(
            sol.zigzagLevelOrder(root),
            [
                [3],
                [20, 9],
                [15, 7]
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
