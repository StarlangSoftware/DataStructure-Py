from __future__ import annotations

from typing import Callable


class BTreeNode:

    K: list
    m: int
    d: int
    leaf: bool
    children: [BTreeNode]

    def __init__(self, d: int, firstChild: BTreeNode = None, secondChild: BTreeNode = None, newK: object = None):
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

    def position(self, value: object, comparator: Callable[[object, object], int]):
        if self.m == 0:
            return 0
        if comparator(value, self.K[self.m - 1]) > 0:
            return  self.m
        else:
            for i in range(self.m):
                if comparator(value, self.K[i]) <= 0:
                    return i
        return -1

    def insertIntoK(self, index: int, insertedK: object):
        if index < len(self.K):
            for i in range(self.m, index, -1):
                self.K[i] = self.K[i - 1]
            self.K[index] = insertedK
        else:
            self.K.append(insertedK)

    def moveHalfOfTheKToNewNode(self, newNode: BTreeNode):
        for i in range(self.d):
            newNode.K.append(self.K[i + self.d + 1])
        newNode.m = self.d

    def moveHalfOfTheChildrenToNewNode(self, newNode: BTreeNode):
        for i in range(self.d):
            newNode.children.append(self.children[i + self.d + 1])

    def moveHalfOfTheElementsToNewNode(self, newNode: BTreeNode):
        self.moveHalfOfTheKToNewNode(newNode)
        self.moveHalfOfTheChildrenToNewNode(newNode)

    def insertNode(self, value: object, comparator: Callable[[object, object], int], isRoot: bool) -> BTreeNode:
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
