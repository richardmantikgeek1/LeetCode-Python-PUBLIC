class Solution:
    def sortArrayByParity(self, array):
        return [a for a in array if a % 2 == 0] + [a for a in array if a % 2 == 1]