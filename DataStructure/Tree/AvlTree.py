from typing import Callable

from DataStructure.Stack import Stack
from DataStructure.Tree.AvlTreeNode import AvlTreeNode
from DataStructure.Tree.Tree import Tree


class AvlTree(Tree):

    def __init__(self, comparator: Callable[[object, object], int]):
        super().__init__(comparator)

    def height(self, d: AvlTreeNode) -> int:
        if d is None:
            return 0
        else:
            return d.height

    def rotateLeft(self, k2: AvlTreeNode) -> AvlTreeNode:
        """
        In rotate left, we move node k1 one level up, since due to the binary search tree
        property k2 > k1, we move node k2 one level down. The links updated are:

        Since k2 > B > k1, the left child of node k2 is now the old right child of k1.

        The right child of k1 is now k2.

        Note that, the root node of the subtree is now k1. In order to modify the parent link of k2, the new root of the
        subtree is returned by the function.
        :param k2: Root of the subtree, which does not satisfy the AVL tree property.
        :return: The new root of the subtree
        """
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), k1.right.height) + 1
        return k1

    def rotateRight(self, k1: AvlTreeNode) -> AvlTreeNode:
        """
        In order to restore the AVL tree property, we move node k2 one level up, since due to the binary search tree
        property k2 > k1, we move node k1 one level down. The links updated are:

        Since k2 > B > k1, the right child of node k1 is now the old left child of k2.

        The left child of k2 is now k1.

        Note that, the root node of the subtree is now k2. In order to modify the parent link of k1, the new root of the subtree is returned by the function.
        :param k1: Root of the subtree, which does not satisfy the AVL tree property.
        :return: The new root of the subtree
        """
        k2 = k1.right
        k1.right = k2.left
        k2.left = k1
        k2.height = max(k2.left.height, self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k2

    def doubleRotateLeft(self, k3: AvlTreeNode):
        """
        In the first phase we will do single right rotation on the subtree rooted with k1. With this rotation, the
        left child of node k2 will be k1, whereas the right child of node k1 will be B (the old left child of node k2).

        In the second phase, we will do single left rotation on the subtree rooted with k3. With this rotation, the
        right child of node k2 will be k3, whereas the left child of node k3 will be C (the old right child of k2).

        Note that, the new root node of the subtree is now k2. In order to modify the parent link of k3, the new root of
        the subtree is returned by the function.
        :param k3: Root of the subtree, which does not satisfy the AVL tree property.
        :return: The new root of the subtree
        """
        k3.left = self.rotateRight(k3.left)
        return self.rotateLeft(k3)

    def doubleRotateRight(self, k1: AvlTreeNode):
        """
        In the first phase we will do single right rotation on the subtree rooted with k3. With this rotation, the right
        child of node k2 will be k3, whereas the left child of node k3 will be C (the old right child of node k2).

        In the second phase, we will do single right rotation on the subtree rooted with k1. With this rotation, the left
        child of node k2 will be k1, whereas the left child of node k1 will be B (the old left child of k2).

        Note that, the new root node of the subtree is now k2. In order to modify the parent link of k1, the new root of
        the subtree is returned by the function.
        :param k1: Root of the subtree, which does not satisfy the AVL tree property.
        :return: The new root of the subtree
        """
        k1.right = self.rotateLeft(k1.right)
        return self.rotateRight(k1)

    def insert(self, node: AvlTreeNode):
        """
        First we will proceed with the stages the same when we add a new node into a binary search tree. For this, we
        start from the root node and traverse in down manner. The current node we visit is represented with x and the
        previous node is represented with y. At each time we compare the value of the current node with the value of the
        new node. If the value of the new node is smaller than the value of the current node, the new node will be
        inserted into the left subtree of the current node. For this, we will continue with the left child to process. If
        the reverse is true, that is, if the value of the new node is larger than the value of the current node, the new
        node will be inserted into the right subtree of the current node. In this case, we will continue with the right
        child to process. At each step, we store the current node in a separate stack.

        When we insert a new node into an AVL tree, we need to change the heights of the nodes and check if the AVL tree
        property is satisfied or not. Only the height of the nodes, which we visit while we are finding the place for the
        new node, can be changed. So, what we should do is to pop those nodes from the stack one by one and change the
        heights of those nodes.

        Similarly, the nodes, which we visit while we are finding the place for the new node, may no longer satisfy the
        AVL tree property. So what we should do is to pop those nodes from the stack one by one and calculate the
        difference of the heights of their left and right subtrees. If the height difference is 2, the AVL tree property
        is not satisfied. If we added the new node into the left subtree of the left child, we need to do left single
        rotation, if we added into the right subtree of the left child, we need to do left double rotation, if we added
        into the left subtree of the right child, we need to do right double rotation, if we added into the right subtree
        of the right child, we need to the right single rotation. Since  the root node of the subtree will be changed
        after a rotation, the new child of y will be the new root node t.
        :param node: Node to be inserted.
        """
        LEFT = 1
        RIGHT = 2
        y = None
        x = self.root
        dir1 = 0
        dir2 = 0
        c = Stack()
        while x is not None:
            y = x
            c.push(y)
            dir1 = dir2
            if self.comparator(node.data, x.data) < 0:
                x = x.left
                dir2 = LEFT
            else:
                x = x.right
                dir2 = RIGHT
        self.insertChild(y, node)
        while not c.isEmpty():
            x = c.pop()
            x.height = max(self.height(x.left), self.height(x.right)) + 1
            if abs(self.height(x.left) - self.height(x.right)) == 2:
                if dir1 == LEFT:
                    if dir2 == LEFT:
                        t = self.rotateLeft(x)
                    else:
                        t = self.doubleRotateLeft(x)
                else:
                    if dir2 == LEFT:
                        t = self.doubleRotateRight(x)
                    else:
                        t = self.rotateRight(x)
                y = c.pop()
                self.insertChild(y, t)
                break

    def insertData(self, data: object):
        self.insert(AvlTreeNode(data))
