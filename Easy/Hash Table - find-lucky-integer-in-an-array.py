class Solution:
    def findLucky(self, array):
        memo = {}
        for i in range(0, len(array)):
            num = array[i]
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1
        
        lucky_nums = []
        for i in range(0, len(array)):
            num = array[i]

            if (memo[num] == num):
                lucky_nums.append(num)
            
        if (len(lucky_nums) > 0):
            return max(lucky_nums)
        else:
            return -1