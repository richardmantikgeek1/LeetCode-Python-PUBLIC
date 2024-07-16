class Solution:
    def numberGame(self, nums):
        arr = []
        while (len(nums) > 0):
            alice_num_value = min(nums)
            alice_num_index = nums.index(alice_num_value)
            nums.pop(alice_num_index)
            bob_num_value = min(nums)
            bob_num_index = nums.index(bob_num_value)
            nums.pop(bob_num_index)
            arr.append(bob_num_value)
            arr.append(alice_num_value)
        
        return arr
    
array = [5,4,2,3]
sol = Solution()
ret_val = sol.numberGame(array)
print(ret_val)