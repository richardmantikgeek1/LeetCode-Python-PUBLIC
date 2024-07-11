# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def minDepth(self, root):
        return self.shortest_path_to_leaf(root)

    def shortest_path_to_leaf(self, node):
        if (node is None): return 0
        elif (node.left is None and node.right is None): return 1
        elif (node.left is not None and node.right is None):
            return 1 + self.shortest_path_to_leaf(node.left)
        elif (node.right is not None and node.left is None):
            return 1 + self.shortest_path_to_leaf(node.right)
        else:
            return 1 + min(self.shortest_path_to_leaf(node.left), self.shortest_path_to_leaf(node.right))
        
        return min_depth

root = TreeNode(5)
left_node = TreeNode(3)
right_node = TreeNode(8)
left_node.left = TreeNode(1)
left_node.right = TreeNode(4)
root.left = left_node
#root.right = right_node
res = Solution().minDepth(None)
print(res)