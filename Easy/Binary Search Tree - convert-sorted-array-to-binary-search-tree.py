# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        ret_val = self.sorted_array_to_bst(nums)
        return ret_val
    
    def sorted_array_to_bst(self, nums):
        if (len(nums) == 0):
            return None
        elif (len(nums) == 1):
            return TreeNode(nums[0])
        else:
            start_index = 0
            end_index = len(nums) - 1
            mid_index = (start_index + end_index) // 2

            ret_val = TreeNode(nums[mid_index])
            ret_val.left = self.sorted_array_to_bst(nums[:mid_index])
            ret_val.right = self.sorted_array_to_bst(nums[mid_index+1:])

            return ret_val
