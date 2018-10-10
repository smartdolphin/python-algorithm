# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = [root]
        while queue:
            [result.append(str(node.val)) if node else result.append('#') for node in queue]
            next_nodes = []
            for node in queue:
                if node:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            queue = next_nodes

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        serialized_data = data.split(',')
        if len(serialized_data) == 0 or serialized_data[0] == '#':
            return None
        root = TreeNode(serialized_data[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if node:
                l_val = serialized_data[index]
                r_val = serialized_data[index + 1]
                node.left = None if l_val == '#' else TreeNode(l_val)
                node.right = None if r_val == '#' else TreeNode(r_val)
                queue.append(node.left)
                queue.append(node.right)
                index += 2
        return root


class TestSerializeAndDeserializeBinaryTree(unittest.TestCase):
    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        codec = Codec()
        self.assertEqual(
            codec.serialize(root),
            '1,2,3,#,#,4,5,#,#,#,#'
        )
        node = codec.deserialize(codec.serialize(root))
        self.assertEqual(
            codec.serialize(node),
            codec.serialize(root)
        )
        root = None
        self.assertEqual(
            codec.serialize(root),
            '#'
        )
        node = codec.deserialize(codec.serialize(root))
        self.assertEqual(
            codec.serialize(node),
            codec.serialize(root)
        )


if __name__ == '__main__':
    unittest.TestCase()
