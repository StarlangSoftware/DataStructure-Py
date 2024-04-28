from typing import Callable

from DataStructure.Tree.TreeNode import TreeNode


class Tree:
    """
    Tree structure is also a non-linear data structure. Different from the tree structure we see in the nature, the
    tree data structure has its root on top and develops its branches down.
    """

    root: TreeNode = None
    comparator: Callable[[object, object], int]

    def __init__(self, comparator: Callable[[object, object], int]):
        """
        Constructor of the tree. According to the comparator, the tree could contain any object.
        :param comparator: Comparator function to compare two elements.
        """
        self.comparator = comparator

    def search(self, value: object) -> TreeNode:
        """
        The search starts from the root node, and we represent the node, with which we compare the searched value, with
        d. If the searched value is equal to the value of the current node, we have found the node we search for, the
        function will return that node. If the searched value is smaller than the value of the current node , the number
        we search for must be on the left subtree of the current node, therefore the new current node must be the left
        child of the current node. As the last case, if the searched value is larger than the value of the current node,
        the number we search for must be on the right subtree of the current node, therefore the new current node must be
        the right child of the current node. If this search continues until the leaf nodes of the tree and we can't find
        the node we search for, node d will be null and the function will return null.
        :param value: Searched value
        :return: If the value exists in the tree, the function returns the node that contains the node. Otherwise, it
        returns null.
        """
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
        """
        Inserts a child to its parent as left or right child.
        :param parent: New parent of the child node.
        :param child: Child node.
        """
        if parent is None:
            self.root = child
        else:
            if self.comparator(child.data, parent.data) < 0:
                parent.left = child
            else:
                parent.right = child

    def insert(self, node: TreeNode):
        """
        In order to add a new node into a binary search tree, we need to first find out the place where we will insert
        the new node. For this, we start from the root node and traverse the tree down. At each step, we compare the
        value of the new node with the value of the current node. If the value of the new node is smaller than the value
        of the current node, the new node will be inserted into the left subtree of the current node. To accomplish this,
        we continue the process with the left child of the current node. If the situation is reverse, that is, if the
        value of the new node is larger than the value of the current node, the new node will be inserted into the right
        subtree of the current node. In this case, we continue the process with the right child of the current node.
        :param node: Node to be inserted.
        """
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
