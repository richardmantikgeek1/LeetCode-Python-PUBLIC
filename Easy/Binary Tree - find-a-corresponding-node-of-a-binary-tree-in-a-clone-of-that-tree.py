# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def getTargetCopy(self, root, cloned, target):
        memo_parent = {}
        memo_parent[root] = None

        self.get_nodes_parent(root, memo_parent)

        target_path = []
        curr_node = target
        while (curr_node is not None):
            parent_node = memo_parent[curr_node]
            if (parent_node is not None and parent_node.left == curr_node):
                target_path.append('left')
            elif (parent_node is not None and parent_node.right == curr_node):
                target_path.append('right')
            curr_node = parent_node
        target_path = list(reversed(target_path))
        target_node = self.find_target_node(cloned, target_path)
        return target_node
        

    def get_nodes_parent(self, node, memo_parent):
        if (node is None):
            memo_parent[None] = None
        else:
            if (node.left is not None):
                memo_parent[node.left] = node
                self.get_nodes_parent(node.left, memo_parent)
            
            if (node.right is not None):
                memo_parent[node.right] = node
                self.get_nodes_parent(node.right, memo_parent)

    def find_target_node(self, node, target_path):
        if (node is None):
            return None
        else:
            if (len(target_path) == 0):
                return node
            elif (len(target_path) > 0):
                if (target_path[0] == 'left'):
                    return self.find_target_node(node.left, target_path[1:])
                elif (target_path[0] == 'right'):
                    return self.find_target_node(node.right, target_path[1:])
        