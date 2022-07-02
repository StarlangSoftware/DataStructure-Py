from __future__ import annotations


class TreeNode:

    data: object
    left: TreeNode = None
    right: TreeNode = None

    def __init__(self, data: object):
        self.data = data
