class Solution:
    def removeDuplicates(self, nums):
        start_index = 0
        last_num = None
        count_uniq_nums = 0
        uniq_nums_map = {}
        while (start_index < len(nums)):
            curr_num = nums[start_index]
            if (curr_num not in uniq_nums_map.keys()):
                count_uniq_nums += 1
            
            uniq_nums_map[curr_num] = True
            start_index += 1
        i = 0
        for k in uniq_nums_map.keys():
            nums[i] = k
            i+=1

        return count_uniq_nums
    
sol = Solution()
array = [1,1,2]
print(sol.removeDuplicates(array))
print(array)