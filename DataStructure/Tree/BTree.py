from typing import Callable

from DataStructure.Tree.BTreeNode import BTreeNode


class BTree:

    root: BTreeNode = None
    comparator: Callable[[object, object], int]
    d: int

    def __init__(self, d: int, comparator: Callable[[object, object], int]):
        self.comparator = comparator
        self.d = d

    def search(self, value: object) -> BTreeNode:
        b = self.root
        while not b.leaf:
            child = b.position(value, self.comparator)
            if child < b.m and b.K[child] == value:
                return b
            b = b.children[child]
        child = b.position(value, self.comparator)
        if child < b.m and b.K[child] == value:
            return b
        return None

    def insertData(self, data: object):
        if self.root is None:
            self.root = BTreeNode(self.d)
        if self.root.leaf:
            s = self.root.insertLeaf(data, self.comparator)
            if s is not None:
                tmp = self.root
                self.root = BTreeNode(self.d, tmp, s, tmp.K[self.d])
        else:
            s = self.root.insertNode(data, self.comparator, True)
            if s is not None:
                self.root = s
