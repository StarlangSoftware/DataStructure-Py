from typing import Callable

from DataStructure.Tree.TreeNode import TreeNode


class Tree:

    root: TreeNode = None
    comparator: Callable[[object, object], int]

    def __init__(self, comparator: Callable[[object, object], int]):
        self.comparator = comparator

    def search(self, value: object) -> TreeNode:
        d = self.root
        while d is not None:
            if self.comparator(d.data, value) == 0:
                return d
            else:
                if self.comparator(d.data, value) > 0:
                    d = d.left
                else:
                    d = d.right
        return None

    def insertChild(self, parent: TreeNode, child: TreeNode):
        if parent is None:
            self.root = child
        else:
            if self.comparator(child.data, parent.data) < 0:
                parent.left = child
            else:
                parent.right = child

    def insert(self, node: TreeNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if self.comparator(node.data, x.data) < 0:
                x = x.left
            else:
                x = x.right
        self.insertChild(y, node)

    def insertData(self, data: object):
        self.insert(TreeNode(data))
