# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        memo_count_val = {}

        inorder_nodes = []

        self.inorder_traversal(root, inorder_nodes, memo_count_val)
        max_count_val = max(memo_count_val.values())

        ret_val = []
        for k in memo_count_val:
            if (memo_count_val[k] == max_count_val):
                ret_val.append(k)
        return ret_val
    
    def inorder_traversal(self, node, inorder_nodes, memo_count_val):
        if (node is None):
            return
        else:
            if (node.left is not None):
                self.inorder_traversal(node.left, inorder_nodes, memo_count_val)
            inorder_nodes.append(node.val)
            if (node.val in memo_count_val.keys()):
                memo_count_val[node.val] += 1
            else:
                memo_count_val[node.val] = 1
            if (node.right is not None):
                self.inorder_traversal(node.right, inorder_nodes, memo_count_val)
        
    