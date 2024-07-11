class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        ret_val = []
        self.preorder_traversal(root, ret_val)
        return ret_val

    def preorder_traversal(self, node, ret_val):
        if (node is None):
            return
        ret_val.append(node.val)
        if (node.left is not None):
            self.preorder_traversal(node.left, ret_val)
        if (node.right is not None):
            self.preorder_traversal(node.right, ret_val)

        