
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p, q):
        return self.is_same_tree(p, q)
    def is_same_tree(self, p, q):
        if (p is None and q is None):
            return True
        elif (p is None and q is not None):
            return False
        elif (p is not None and q is None):
            return False
        elif (p.val != q.val):
            return False
        elif (p.val == q.val):
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        
root_1 = TreeNode(5)
left_node_1 = TreeNode(3)
right_node_1 = TreeNode(8)
left_node_1.left = TreeNode(1)
left_node_1.right = TreeNode(4)
root_1.left = left_node_1
root_1.right = right_node_1

root_2 = TreeNode(5)
left_node_2 = TreeNode(3)
right_node_2 = TreeNode(8)
left_node_2.left = TreeNode(1)
left_node_2.right = TreeNode(4)
root_2.left = left_node_2
root_2.right = right_node_2

res_1 = Solution().isSameTree(root_1, root_2)
print(res_1)