# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start_index = 1
        end_index = n
        return self.first_bad_version(n, start_index, end_index)
    
    def first_bad_version(self, n, start_index, end_index):
        mid_index = (start_index + end_index) // 2
        if (not isBadVersion(mid_index-1) and isBadVersion(mid_index)):
            return mid_index
        
        if (isBadVersion(mid_index)):
            return self.first_bad_version(mid_index, 1, mid_index)
        elif (not isBadVersion(mid_index)):
            return self.first_bad_version(n, mid_index+1, n)