class Solution:
    def findKDistantIndices(self, array, key, k):
        ret_val = {}
        j = 0
        while (j < len(array)):
            if (array[j] == key):
                for i in range(0, len(array)):
                    if (abs(i - j) <= k and i not in ret_val.keys()):
                        ret_val[i] = True
            j += 1
        return sorted(ret_val.keys())
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
sol = Solution()
ret_val = sol.findKDistantIndices(nums, key, k)
print(ret_val)