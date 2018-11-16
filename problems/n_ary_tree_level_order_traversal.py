# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal
import unittest


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            tmp, next_nodes = [], []
            for node in queue:
                next_nodes += node.children
                tmp.append(node.val)
            result.append(tmp)
            queue = next_nodes
        return result


class TestLevelOrder(unittest.TestCase):
    def test(self):
        root = Node(1)
        root.children = [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]

        sol = Solution()
        self.assertEqual(
            sol.levelOrder(root),
            [
                [1],
                [3, 2, 4],
                [5, 6],
            ]
        )


if __name__ == '__main__':
    unittest.TestCase()
