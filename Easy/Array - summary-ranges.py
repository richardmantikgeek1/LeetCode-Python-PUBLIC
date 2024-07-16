from collections import deque

class Solution:
    def summaryRanges(self, nums):
        nums = sorted(nums)

        memo = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if ((num-1) in memo.keys()):
                seq = memo[num-1]
                seq_copy = seq.copy()
                seq_copy.append(num)
                memo[num] = seq_copy
                
                memo.pop(num-1)
            else:
                seq = deque()
                seq_copy = seq.copy()
                seq_copy.append(num)
                if (num not in memo.keys()):
                    memo[num] = seq_copy
        
        ret_val = []
        for key in memo.keys():
            seq = memo[key]
            if (len(seq) > 1):
                ret_val.append(str(seq[0]) + '->' + str(seq[len(seq)-1]))
            else:
                ret_val.append(str(seq[0]))

        return ret_val