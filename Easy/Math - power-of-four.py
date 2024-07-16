import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n <= 0):
            return False

        x = math.ceil(math.log(n, 4))
        return n == 4 ** x