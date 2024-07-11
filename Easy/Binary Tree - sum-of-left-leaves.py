# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        left_leaves = []
        self.fetch_left_leaves(root, left_leaves)
        return sum([n.val for n in left_leaves])
    
    def fetch_left_leaves(self, node, left_leaves):
        if (node is None):
            return
        else:
            if (node.left is not None):
                if (node.left.left is None and node.left.right is None):
                    left_leaves.append(node.left)
                self.fetch_left_leaves(node.left, left_leaves)
            if (node.right is not None):
                self.fetch_left_leaves(node.right, left_leaves)