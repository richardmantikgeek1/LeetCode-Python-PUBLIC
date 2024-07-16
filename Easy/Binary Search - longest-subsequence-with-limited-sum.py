class Solution:
    def answerQueries(self, nums, queries):
        nums = sorted(nums)
        prefix_sum = 0
        memo = []
        for i in range(0, len(nums)):
            num = nums[i]
            memo.append(prefix_sum)
            prefix_sum += num
        memo.append(prefix_sum)

        ret_val = []
        for i in range(0, len(queries)):
            q = queries[i]
            prefix_index = self.binary_search_iterative(memo, q)
            ret_val.append(prefix_index)
        
        return ret_val

    def binary_search_iterative(self, memo, target):
        start_index = 0
        end_index = len(memo) - 1
        while (start_index <= end_index):
            mid_index = (start_index + end_index) // 2
            if (mid_index == len(memo)-1 and target >= memo[mid_index]):
                return mid_index
            elif (target >= memo[mid_index] and target < memo[mid_index+1]):
                return mid_index
            elif (target < memo[mid_index]):
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        return -1

memo = [0,1,3,7,12]
queries = [3,10,21]
sol = Solution()
print(sol.binary_search_iterative(memo, 21))