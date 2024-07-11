# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        ret_val = []
        self.level_order_traversal(root, ret_val)
        is_sum_found = False
        for s in [sum(array) for array in ret_val]:
            if s == targetSum:
                return True
        return is_sum_found
    
    def level_order_traversal(self, node, ret_val):
        level_order_nodes = []
        if (node is not None):
            level_order_nodes.append([node])
            while (len(level_order_nodes) > 0):
                nodes_list = level_order_nodes.pop(0)
                level_nodes = []
                n = nodes_list[len(nodes_list) - 1]
                if (n.left is None and n.right is None): # leaf node
                    ret_val.append([nn.val for nn in nodes_list])
                else:
                    if (n.left is not None):
                        level_nodes.append(nodes_list + [n.left])
                    if (n.right is not None):
                        level_nodes.append(nodes_list + [n.right])
                    if (len(level_nodes) > 0):
                        level_order_nodes.extend(level_nodes)

root = TreeNode(5)
left_node = TreeNode(3)
right_node = TreeNode(8)
left_node.left = TreeNode(1)
left_node.right = TreeNode(4)
root.left = left_node
root.right = right_node
res = Solution().hasPathSum(None, 0)
print(res)