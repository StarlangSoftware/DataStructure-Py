from DataStructure.Tree.TreeNode import TreeNode


class AvlTreeNode(TreeNode):

    height: int

    def __init__(self, data: object):
        super().__init__(data)
        self.height = 1
