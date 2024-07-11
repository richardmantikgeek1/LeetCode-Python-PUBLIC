# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root_1, root_2):
        dummy_node_1 = TreeNode(0)
        dummy_node_1.left = None
        dummy_node_1.right = root_1
        
        dummy_node_2 = TreeNode(0)
        dummy_node_2.left = None
        dummy_node_2.right = root_2
        self.merge_trees(dummy_node_1, dummy_node_2)

        return dummy_node_1.right

    def merge_trees(self, node_1, node_2):
        if (node_1 is None or node_2 is None):
            return
        else:
            if (node_1.left is not None
                and node_1.right is not None):
                node_1.val = node_1.val + node_2.val
                self.merge_trees(node_1.left, node_2.left)
                self.merge_trees(node_1.right, node_2.right)
            else:
                node_1.val = node_1.val + node_2.val
                if (node_1.left is None
                    and node_2.left is not None):
                    node_1.left = TreeNode(0)
                self.merge_trees(node_1.left, node_2.left)
                if (node_1.right is None
                    and node_2.right is not None):
                    node_1.right = TreeNode(0)
                self.merge_trees(node_1.right, node_2.right)
            
            
