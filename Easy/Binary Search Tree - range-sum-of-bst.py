# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node, low, high):
        array = []
        self.inorder_traversal(node, array, low, high)
        return sum(array)
        
    def inorder_traversal(self, node, array, low, high):
        if (node is None):
            return
        if (node.left is not None and node.val >= low):
            self.inorder_traversal(node.left, array, low, high)
        if (low <= node.val <= high):
            array.append(node.val)
        if (node.right is not None and node.val <= high):
            self.inorder_traversal(node.right, array, low, high)