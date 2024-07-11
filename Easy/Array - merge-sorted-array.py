class Solution:
    def merge(self, array_1, m, array_2, n):
        nums_1 = array_1[0:m]
        nums_2 = array_2[::] 
        nums_1.extend(nums_2)
        nums_1.sort()
        for i in range(0, m+n):
            array_1[i] = nums_1[i]

sol = Solution()
array_1 = [1,2,3,0,0,0]
array_2 = [2,5,6]
sol.merge(array_1, 3, array_2, 3)
print(array_1)