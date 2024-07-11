class Solution:
    def divideArray(self, array):
        memo = {}
        for i in range(0, len(array)):
            num = array[i]
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1

        for num in memo.keys():
            if memo[num] % 2 != 0:
                return False
        
        return True