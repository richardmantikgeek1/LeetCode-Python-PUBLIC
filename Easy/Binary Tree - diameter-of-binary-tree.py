# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        level_order_nodes = []
        self.level_order_traversal(root, level_order_nodes)
        
        memo_len_path = {}
        memo_len_graph = {}
        for level_nodes in reversed(level_order_nodes):
            for n in reversed(level_nodes):
                if (n.left is None
                    and n.right is None):
                    memo_len_path[n] = 1
                    memo_len_graph[n] = 1
                else:
                    lpl = 0
                    if (n.left in memo_len_path.keys()):
                        lpl = memo_len_path[n.left]
                    lpr = 0
                    if (n.right in memo_len_path.keys()):
                        lpr = memo_len_path[n.right]
                    memo_len_path[n] = max(1, 1 + lpl, 1 + lpr)
                    memo_len_graph[n] = max(1, 1 + lpl, 1 + lpr, 1 + lpl + lpr)
                
        
        return max(list(memo_len_graph.values())) - 1

        

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