# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal
import unittest


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    # recursive
    # time: O(n), space: O(n)
    def preorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node is None:
            return
        result.append(node.val)
        for child_node in node.children:
            self.helper(child_node, result)

    # iterative
    # time: O(n), space: O(1)
    def preorder(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child_node in reversed(node.children):
                stack.append(child_node)
        return result


class TestNAryTreePreOrder(unittest.TestCase):
    def test(self):
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        sol = Solution()
        self.assertEqual(
            sol.preorder(root),
            [1, 3, 5, 6, 2, 4]
        )


if __name__ == '__main__':
    unittest.TestCase()
