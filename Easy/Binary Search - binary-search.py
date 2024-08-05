class Solution:
    def search(self, nums, target):
        start_index = self.binary_search(nums, target)
        if (start_index is not None):
            return start_index
        else:
            return -1
    
    def binary_search(self, nums, target):
        start_index = 0
        end_index = len(nums) - 1

        mid_index = (start_index + end_index) // 2
        while (start_index <= end_index):
            if (nums[mid_index] == target):
                for i in range(mid_index-1, -1, -1):
                    if (nums[i] == nums[mid_index]):
                        mid_index = i
                    else:
                        break
                return mid_index
            elif (nums[mid_index] > target):
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
            mid_index = (start_index + end_index) // 2
        
        return None