# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        level_order_nodes = []
        self.level_order_traversal(root, level_order_nodes)

        memo_tree_sum = {}
        memo_tree_tilt = {}
        for level_nodes in reversed(level_order_nodes):
            for n in reversed(level_nodes):
                if (n.left is None
                    and n.right is None):
                    memo_tree_sum[n] = n.val
                    memo_tree_tilt[n] = 0
                else:
                    tsl = 0
                    if (n.left in memo_tree_sum.keys()):
                        tsl = memo_tree_sum[n.left]
                    tsr = 0
                    if (n.right in memo_tree_sum.keys()):
                        tsr = memo_tree_sum[n.right]
                    memo_tree_sum[n] = n.val + tsl + tsr
                    memo_tree_tilt[n] = abs(tsl - tsr)

        return sum(memo_tree_tilt.values())

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
        