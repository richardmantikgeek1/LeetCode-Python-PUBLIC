# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        ret_val = []
        self.postorder_traversal(root, ret_val)
        return ret_val

    def postorder_traversal(self, node, ret_val):
        if (node is None):
            return
        if (node.left is not None):
            self.postorder_traversal(node.left, ret_val)
        if (node.right is not None):
            self.postorder_traversal(node.right, ret_val)
        ret_val.append(node.val)
