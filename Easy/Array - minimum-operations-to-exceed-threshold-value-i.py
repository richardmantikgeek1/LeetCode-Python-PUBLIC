class Solution:
    def minOperations(self, array, k):
        return len([a for a in array if a < k])