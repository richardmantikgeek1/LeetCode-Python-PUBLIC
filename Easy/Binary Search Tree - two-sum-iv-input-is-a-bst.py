# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, target) -> bool:
        inorder_nodes = []

        self.inorder_traversal(root, inorder_nodes)

        memo = {}
        for i in range(0, len(inorder_nodes)):
            n = inorder_nodes[i]
            complement = target - n.val

            if (complement in memo.keys() and memo[complement] < i):
                return True

            memo[n.val] = i

    def inorder_traversal(self, node, inorder_nodes):
        if (node is None):
            return
        else:
            if (node.left is not None):
                self.inorder_traversal(node.left, inorder_nodes)
            inorder_nodes.append(node)
            if (node.right is not None):
                self.inorder_traversal(node.right, inorder_nodes)