class Solution:
    def missingNumber(self, array):
        memo = {}
        for i in range(0, len(array)):
            num = array[i]
            memo[num] = True

        min_num = min(array)
        max_num = max(array)
        if (min_num > 0):
            return 0
        else:
            num = min_num
            while (num <= max_num):
                if (num not in memo.keys()):
                    return num

                num += 1
            return max_num+1