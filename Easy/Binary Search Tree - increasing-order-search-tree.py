# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_nodes = []

        self.inorder_traversal(root, inorder_nodes)

        ret_val = self.build_increasing_BST(inorder_nodes)
        return ret_val
    
    def inorder_traversal(self, node, inorder_nodes):
        if (node is None):
            return
        else:
            if (node.left is not None):
                self.inorder_traversal(node.left, inorder_nodes)
            inorder_nodes.append(node)
            if (node.right is not None):
                self.inorder_traversal(node.right, inorder_nodes)

    def build_increasing_BST(self, inorder_nodes):
        dummy_node = TreeNode(None)
        node = dummy_node
        for n in inorder_nodes:
            node.right = TreeNode(n.val)
            node.left = None
            node = node.right
        
        return dummy_node.right