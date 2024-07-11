# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        if (root is None):
            return True
        else:
            ret_val = abs(self.height_of_tree(root.left) - self.height_of_tree(root.right)) <= 1 
            ret_val = ret_val and self.isBalanced(root.left)
            ret_val = ret_val and self.isBalanced(root.right)

            return ret_val

    def height_of_tree(self, node):
        if (node is None):
            return 0
        else:
            return 1 + max(self.height_of_tree(node.left), self.height_of_tree(node.right))