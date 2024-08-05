class Solution:
    def findDisappearedNumbers(self, array):
        for num in array:
            i = abs(num) - 1
            array[i] = -1 * abs(array[i])

        ret_val = []
        for i in range(0, len(array)):
            if (array[i] > 0):
                ret_val.append(i + 1)
        return ret_val

array = [4,3,2,7,8,2,3,1]
sol = Solution()
result = sol.findDisappearedNumbers(array)
print(result)