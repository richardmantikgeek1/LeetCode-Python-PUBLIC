class Solution:
    def canBeEqual(self, target, array):
        return sorted(target) == sorted(array)