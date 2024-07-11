# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        ret_val = []
        self.inorder_traversal(root, ret_val)
        return ret_val
    
    def inorder_traversal(self, node, ret_val):
        if (node is None):
            return
        if (node.left is not None):
            self.inorder_traversal(node.left, ret_val)
        ret_val.append(node.val)
        if (node.right is not None):
            self.inorder_traversal(node.right, ret_val)