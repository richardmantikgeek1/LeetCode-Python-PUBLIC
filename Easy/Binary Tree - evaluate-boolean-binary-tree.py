# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, node):
        if (node.left is None and node.right is None):
            return node.val
        else:
            left_val = None
            if (node.left is not None):
                left_val = self.evaluateTree(node.left)

            right_val = None
            if (node.right is not None):
                right_val = self.evaluateTree(node.right)

            if (node.val == 2): # OR
                if (left_val == 0 and right_val == 0): # False OR False
                    return 0
                else:
                    return 1
            elif (node.val == 3): # AND
                if (left_val == 1 and right_val == 1): # True and True
                    return 1
                else:
                    return 0
