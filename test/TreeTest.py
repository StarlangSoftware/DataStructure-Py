import unittest

from DataStructure.Tree.AvlTree import AvlTree
from DataStructure.Tree.BTree import BTree
from DataStructure.Tree.Tree import Tree


class MyTestCase(unittest.TestCase):

    def test_tree(self):
        tree = Tree(lambda x1, x2: 1 if x1>x2 else (0 if x1 == x2 else -1))
        tree.insertData(4)
        tree.insertData(6)
        tree.insertData(2)
        tree.insertData(5)
        tree.insertData(3)
        tree.insertData(1)
        tree.insertData(7)
        self.assertIsNotNone(tree.search(3))
        self.assertIsNone(tree.search(8))

    def test_tree2(self):
        tree = AvlTree(lambda x1, x2: 1 if x1>x2 else (0 if x1 == x2 else -1))
        for i in range(1, 32):
            tree.insertData(i)
        for i in range(1, 32):
            self.assertIsNotNone(i)
        self.assertIsNone(tree.search(32))

    def test_tree3(self):
        tree = BTree(1, lambda x1, x2: 1 if x1>x2 else (0 if x1 == x2 else -1))
        for i in range(1, 32):
            tree.insertData(i)
        for i in range(1, 32):
            self.assertIsNotNone(i)
        self.assertIsNone(tree.search(32))


if __name__ == '__main__':
    unittest.main()
