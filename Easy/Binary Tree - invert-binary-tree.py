# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        self.invert_tree(root)
        return root
    
    def invert_tree(self, node):
        if (node is None):
            return
        else:
            node.left, node.right = node.right, node.left
            self.invert_tree(node.left)
            self.invert_tree(node.right)