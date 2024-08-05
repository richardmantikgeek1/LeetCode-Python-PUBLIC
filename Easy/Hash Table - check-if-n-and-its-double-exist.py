class Solution:
    def checkIfExist(self, array):
        memo = {}
        for i in range(0, len(array)):
            num = array[i]
            memo[num] = i

        for i in range(0, len(array)):
            num = array[i]
            double_num = 2 * num
            if (double_num in memo.keys() and memo[double_num] != i):
                return True

        return False