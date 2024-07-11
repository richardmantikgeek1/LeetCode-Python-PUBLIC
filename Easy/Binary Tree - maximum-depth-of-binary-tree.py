# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        return self.max_depth(root)

    def max_depth(self, node):
        if (node is None): return 0

        max_depth = 0
        max_depth_left = 0
        max_depth_right = 0
        if (node.left is not None):
            max_depth_left = self.max_depth(node.left)
        if (node.right is not None):
            max_depth_right = self.max_depth(node.right)

        max_depth = 1 + max(max_depth_left, max_depth_right)
        return max_depth

root = TreeNode(5)
left_node = TreeNode(3)
right_node = TreeNode(8)
left_node.left = TreeNode(1)
left_node.right = TreeNode(4)
root.left = left_node
root.right = right_node
res = Solution().maxDepth(None)
print(res)