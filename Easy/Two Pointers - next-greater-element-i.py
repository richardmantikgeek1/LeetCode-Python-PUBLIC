class Solution:
    def nextGreaterElement(self, nums_1, nums_2):
        i = 0
        j = i + 1
        ret_val = []
        while (i < len(nums_1)):
            j = 0
            while (j < len(nums_2) and nums_1[i] != nums_2[j]):
                j += 1
            while (j < len(nums_2) and nums_1[i] >= nums_2[j]):
                j += 1
            if (j < len(nums_2)):
                ret_val.append(nums_2[j])
            else:
                ret_val.append(-1)
            i += 1

        return ret_val

sol = Solution()
nums_1 = [4,1,2]
nums_2 = [1,3,4,2]
print(sol.nextGreaterElement(nums_1, nums_2))