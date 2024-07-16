class Solution:
    def containsDuplicate(self, array):
        memo = {}
        for num in array:
            if (num in memo.keys()):
                return True

            memo[num] = True

        return False