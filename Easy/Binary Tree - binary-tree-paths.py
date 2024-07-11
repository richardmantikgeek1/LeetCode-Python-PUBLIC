# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        memo_parent = {}
        memo_parent[root] = None

        memo_paths = {}
        self.get_nodes_parent(root, memo_parent, memo_paths)
        return memo_paths.values()
    
    def get_nodes_parent(self, node, memo_parent, memo_paths):
        if (node is None):
            memo_parent[None] = None
        else:
            if (node.left is not None):
                memo_parent[node.left] = node
                self.get_nodes_parent(node.left, memo_parent, memo_paths)
            
            if (node.right is not None):
                memo_parent[node.right] = node
                self.get_nodes_parent(node.right, memo_parent, memo_paths)

            if (node.left is None
                and node.right is None):
                n_ancestors = []
                n_parent = node
                while (n_parent is not None):
                    n_ancestors.append(n_parent)
                    n_parent = memo_parent[n_parent]
                
                memo_paths[node] = '->'.join(reversed([str(n.val) for n in n_ancestors]))