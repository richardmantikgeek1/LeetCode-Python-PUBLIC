# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        level_order_nodes = []
        self.level_order_traversal(root, level_order_nodes)
        for level_nodes in reversed(level_order_nodes):
            for n in reversed(level_nodes):
                if (self.is_same_subtree(n, subRoot)):
                    return True
        
        return False
    
    def is_same_subtree(self, node, subroot):
        if (node is None and subroot is None):
            return True
        elif (node is None and subroot is not None):
            return False
        elif (node is not None and subroot is None):
            return False
        else:
            if node.val == subroot.val:
                return self.is_same_subtree(node.left, subroot.left) and self.is_same_subtree(node.right, subroot.right)
            else:
                return False
            
    def level_order_traversal(self, node, ret_val):
        level_order_nodes = []
        if (node is not None):
            level_order_nodes.append([node])
            ret_val.append([node])
            while (len(level_order_nodes) > 0):
                nodes_list = level_order_nodes.pop(0)
                level_nodes = []
                for n in nodes_list:
                    if (n.left is not None):
                        level_nodes.append(n.left)
                    if (n.right is not None):
                        level_nodes.append(n.right)

                if (len(level_nodes) > 0):
                    level_order_nodes.append(level_nodes)
                    ret_val.append(level_nodes)
