"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        ret_val = []
        self.preorder_traversal(root, ret_val)
        return ret_val
    
    def preorder_traversal(self, node, ret_val):
        if (node is None): return
        ret_val.append(node.val)
        for n in node.children:
            if (n is not None):
                self.preorder_traversal(n, ret_val)