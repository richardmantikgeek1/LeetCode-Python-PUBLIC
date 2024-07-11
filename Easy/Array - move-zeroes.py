class Solution:
    def moveZeroes(self, array):
        new_array = [a for a in array if a != 0] + [a for a in array if a == 0]
        array[:] = new_array


sol = Solution()
print(sol.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
        