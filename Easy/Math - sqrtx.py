class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        last_n = None
        while n**2 <= x:
            last_n = n
            n+=1
        if (last_n is not None):
            return last_n
        else:
            return 0