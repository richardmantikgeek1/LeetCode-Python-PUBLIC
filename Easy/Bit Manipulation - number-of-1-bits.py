class Solution:
    def hammingWeight(self, n):
        return format(n, 'b').count('1')