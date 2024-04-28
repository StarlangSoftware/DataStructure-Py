from typing import Callable

from DataStructure.Tree.BTreeNode import BTreeNode


class BTree:

    root: BTreeNode = None
    comparator: Callable[[object, object], int]
    d: int

    def __init__(self, d: int, comparator: Callable[[object, object], int]):
        """
        Constructor of the tree. According to the comparator, the tree could contain any object.
        :param d: Parameter d in d-ary tree.
        :param comparator: Comparator function to compare two elements.
        """
        self.comparator = comparator
        self.d = d

    def search(self, value: object) -> BTreeNode:
        """
        We start searching from the root node, the node with which we compare the searched value at each stage is
        represented by b, and we continue the search until we arrive the leaf nodes. In order to understand the subtree
        of node b where our searched value resides, we need to compare the searched value with the values Ki. For this,
        the function named position is given. If the searched value is larger than the last value of node b, we need to
        continue the search with the rightmost child. If the searched value is smaller than the i. value of node b, we
        need to continue the search with the i. child. As a last step, the function returns the leaf node of node b.
        :param value: Value searched in B+ tree.
        :return: If the value exists in the tree, the function returns the node that contains the node. Otherwise, it
        returns null.
        """
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
