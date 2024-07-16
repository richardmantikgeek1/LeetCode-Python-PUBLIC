class Elem:
    def __init__(self, index, value):
        self.index = index
        self.value = value
    def __str__(self):
        return '(' + str(self.index) + ', ' + str(self.value) + ')'

from functools import cmp_to_key
class Solution:
    def minimumCost(self, nums):
        elems = []
        for i in range(0, len(nums)):
            num = nums[i]
            elem = Elem(i, num)
            elems.append(elem)

        elems = sorted(elems, key=cmp_to_key(self.my_compare))
        elems = elems[:3]
        
        if (0 not in [e.index for e in elems]):
            max_elem = max(elems, key=cmp_to_key(self.my_compare))
            elems.pop(elems.index(max_elem))
            elem = Elem(0, nums[0])
            elems.insert(0, elem)

        ret_val = 0
        for e in elems:
            ret_val += e.value
        
        return ret_val

    def my_compare (self, subarray_1, subarray_2):
        if subarray_1.value < subarray_2.value:
            return -1
        else:
            return 1
        

nums = [12, 1,2,3]
nums = [10,3,1,1]
nums = [1,2,3,12]
nums = [1,5,1,5]
nums = [21,17,6,31,10,6,1,31,3,35]
sol = Solution()
result = sol.minimumCost(nums)
print(result)