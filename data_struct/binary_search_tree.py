import unittest


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return not self.left and not self.right

    def has_left(self):
        return not (self.left is None)

    def has_right(self):
        return not (self.right is None)

    def children_count(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            if self.find(value) is not None:
                print('Duplicated value: ', value)
                return
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = TreeNode(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)
        else:
            return None

    def init_tree(self):
        self.root = None

    def delete(self, value):
        self.root, deleted = self._delete_value(self.root, value)
        return deleted

    def _delete_value(self, node, value):
        if node is None:
            return node, False

        deleted = False
        if value == node.value:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif value < node.value:
            node.left, deleted = self._delete_value(node.left, value)
        else:
            node.right, deleted = self._delete_value(node.right, value)
        return node, deleted

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)

    def traverse(self, order='in'):
        result = []
        if self.root is not None:
            if order == 'in':
                self._in_order(self.root, result)
            elif order == 'pre':
                self._pre_order(self.root, result)
            elif order == 'post':
                self._post_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node.left is not None:
            self._in_order(node.left, result)
        result.append(node.value)
        if node.right is not None:
            self._in_order(node.right, result)

    def _pre_order(self, node, result):
        result.append(node.value)
        if node.left is not None:
            self._pre_order(node.left, result)
        if node.right is not None:
            self._pre_order(node.right, result)

    def _post_order(self, node, result):
        if node.left is not None:
            self._post_order(node.left, result)
        if node.right is not None:
            self._post_order(node.right, result)
        result.append(node.value)


class TestBinaryTree(unittest.TestCase):
    def test(self):
        tree = BinarySearchTree()
        tree.add(4)
        tree.add(5)
        tree.add(0)
        tree.add(-1)
        tree.add(8)
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(4)
        tree.print_tree()
        self.assertEqual(tree.find(-1).value, -1)
        self.assertEqual(tree.find(0).value, 0)
        self.assertEqual(tree.find(1).value, 1)
        self.assertEqual(tree.find(2).value, 2)
        self.assertEqual(tree.find(3).value, 3)
        self.assertEqual(tree.find(4).value, 4)
        self.assertEqual(tree.find(5).value, 5)
        self.assertEqual(tree.find(8).value, 8)
        self.assertEqual(tree.find(-2), None)
        self.assertEqual(tree.find(10), None)
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 0, 1, 2, 3, 4, 5, 8]
        )
        self.assertEqual(
            tree.traverse(order='pre'),
            [4, 0, -1, 2, 1, 3, 5, 8]
        )
        self.assertEqual(
            tree.traverse(order='post'),
            [-1, 1, 3, 2, 0, 8, 5, 4]
        )
        self.assertTrue(tree.delete(4))
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 0, 1, 2, 3, 5, 8]
        )
        self.assertTrue(tree.delete(8))
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 0, 1, 2, 3, 5]
        )
        self.assertTrue(tree.delete(0))
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 1, 2, 3, 5]
        )
        self.assertTrue(tree.delete(3))
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 1, 2, 5]
        )
        self.assertTrue(tree.delete(2))
        self.assertEqual(
            tree.traverse(order='in'),
            [-1, 1, 5]
        )
        self.assertTrue(tree.delete(-1))
        self.assertTrue(tree.delete(1))
        self.assertEqual(
            tree.traverse(order='in'),
            [5]
        )
        self.assertTrue(tree.delete(5))
        self.assertEqual(
            tree.traverse(order='in'),
            []
        )
        self.assertFalse(tree.delete(0))


if __name__ == '__main__':
    unittest.TestCase()
