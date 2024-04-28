from __future__ import annotations

from typing import Callable


class BTreeNode:

    K: list
    m: int
    d: int
    leaf: bool
    children: [BTreeNode]

    def __init__(self, d: int, firstChild: BTreeNode = None, secondChild: BTreeNode = None, newK: object = None):
        """
        Another constructor of a B+ Tree node. By default, it is not a leaf node. Adds two children.
        :param d: d in d-ary tree.
        :param firstChild: First child of the root node.
        :param secondChild: Second child of the root node.
        :param newK: First value in the node.
        """
        self.d = d
        self.K = []
        self.children = []
        if firstChild is None:
            self.m = 0
            self.leaf = True
        else:
            self.leaf = False
            self.m = 1
            self.children.append(firstChild)
            self.children.append(secondChild)
            self.K.append(newK)

    def position(self, value: object, comparator: Callable[[object, object], int]) -> int:
        """
        Searches the position of value in the list K. If the searched value is larger than the last value of node, we
        need to continue the search with the rightmost child. If the searched value is smaller than the i. value of node,
        we need to continue the search with the i. child.
        :param value: Searched value
        :param comparator: Comparator function which compares two elements.
        :return: The position of searched value in array K.
        """
        if self.m == 0:
            return 0
        if comparator(value, self.K[self.m - 1]) > 0:
            return self.m
        else:
            for i in range(self.m):
                if comparator(value, self.K[i]) <= 0:
                    return i
        return -1

    def insertIntoK(self, index: int, insertedK: object):
        """
        Add the new value insertedK to the array K into the calculated position index.
        :param index: Place to insert new value
        :param insertedK: New value to be inserted.
        """
        if index < len(self.K):
            for i in range(self.m, index, -1):
                self.K[i] = self.K[i - 1]
            self.K[index] = insertedK
        else:
            self.K.append(insertedK)

    def moveHalfOfTheKToNewNode(self, newNode: BTreeNode):
        """
        Transfers the last d values of the current node to the newNode.
        :param newNode: New node.
        """
        for i in range(self.d):
            newNode.K.append(self.K[i + self.d + 1])
        newNode.m = self.d

    def moveHalfOfTheChildrenToNewNode(self, newNode: BTreeNode):
        """
        Transfers the last d links of the current node to the newNode.
        :param newNode: New node.
        """
        for i in range(self.d):
            newNode.children.append(self.children[i + self.d + 1])

    def moveHalfOfTheElementsToNewNode(self, newNode: BTreeNode):
        """
        Transfers the last d values and the last d links of the current node to the newNode.
        :param newNode: New node.
        """
        self.moveHalfOfTheKToNewNode(newNode)
        self.moveHalfOfTheChildrenToNewNode(newNode)

    def insertNode(self, value: object, comparator: Callable[[object, object], int], isRoot: bool) -> BTreeNode:
        """
        First the function position is used to determine the node or the subtree to which the new node will be added.
        If this subtree is a leaf node, we call the function insertLeaf that will add the value to a leaf node. If this
        subtree is not a leaf node the function calls itself with the determined subtree. Both insertNode and insertLeaf
        functions, if adding a new value/node to that node/subtree necessitates a new child node to be added to the
        parent node, they will both return the new added node and the node obtained by dividing the original node. If
        there is not such a restructuring, these functions will return null. If we add a new child node to the parent
        node, first we open a space for that child node in the value array K, then we add this new node to the array K.
        After adding there are two possibilities:

        After inserting the new child node, the current node did not exceed its capacity. In this case, we open
        space for the link, which points to the new node, in the array children and place that link inside of this
        array.

        After inserting the new child node, the current node exceed its capacity. In this case, we need to create
        newNode, transfer the last d values and the last d links of the current node to the newNode. As a last case,
        if the divided node is the root node, we need to create a new root node and the first child of this new root
        node will be b, and the second child of the new root node will be newNode.
        :param value: Value to be inserted into B+ tree.
        :param comparator: Comparator function to compare two elements.
        :param isRoot: If true, value is inserted as a root node, otherwise false.
        :return: If inserted node results in a creation of a node, the function returns that node, otherwise null.
        """
        child = self.position(value, comparator)
        if not self.children[child].leaf:
            s = self.children[child].insertNode(value, comparator, False)
        else:
            s = self.children[child].insertLeaf(value, comparator)
        if s is None:
            return None
        self.insertIntoK(child, self.children[child].K[self.d])
        if self.m < 2 * self.d:
            self.children.append(s)
            self.m = self.m + 1
            return None
        else:
            newNode = BTreeNode(self.d)
            newNode.leaf = False
            self.moveHalfOfTheElementsToNewNode(newNode)
            newNode.children.append(s)
            self.m = self.d
            if isRoot:
                a = BTreeNode(self.d, self, newNode, self.K[self.d])
                return a
            else:
                return newNode

    def insertLeaf(self, value: object, comparator: Callable[[object, object], int]) -> BTreeNode:
        """
        First the function position is used to determine the position where the new value will be placed Then we open a
        space for that value in the value array K, then we add this new value to the array K into the calculated
        position. At this stage there are again two possibilities:

        After inserting the new value, the current leaf node did not exceed its capacity. The function returns
        null.

        After inserting the new value, the current leaf node exceed its capacity. In this case, we need to create
        the newNode, and transfer the last d values of node b to this newNode.
        :param value: Value to be inserted into B+ tree.
        :param comparator: Comparator function to compare two elements.
        :return: If inserted node results in a creation of a node, the function returns that node, otherwise null.
        """
        child = self.position(value, comparator)
        self.insertIntoK(child, value)
        if self.m < 2 * self.d:
            self.m = self.m + 1
            return None
        else:
            newNode = BTreeNode(self.d)
            self.moveHalfOfTheKToNewNode(newNode)
            self.m = self.d
            return newNode
