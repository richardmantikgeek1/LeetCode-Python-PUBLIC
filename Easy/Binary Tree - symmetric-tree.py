class Solution:
    def isSymmetric(self, root):
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, p, q):
        if (p is None and q is None):
            return True
        elif (p is None and q is not None):
            return False
        elif (p is not None and q is None):
            return False
        elif (p.val != q.val):
            return False
        elif (p.val == q.val):
            return self.is_mirror(p.left, q.right) and self.is_mirror(p.right, q.left)
    
    def my_inorder_traversal(self, node, ret_val):
        if (node is None): return
        
        if (node.left is not None):
            self.my_inorder_traversal(node.left, ret_val)
        ret_val.append(node.val)
        if (node.right is not None):
            self.my_inorder_traversal(node.right, ret_val)
root_1 = TreeNode(5)
left_node_1 = TreeNode(3)
right_node_1 = TreeNode(3)
left_node_1.left = TreeNode(1)
left_node_1.right = TreeNode(4)

right_node_1.left = TreeNode(4)
right_node_1.right = TreeNode(1)

root_1.left = left_node_1
root_1.right = right_node_1
ret_val = []
res_1 = Solution().my_inorder_traversal(root_1, ret_val)
print(ret_val)