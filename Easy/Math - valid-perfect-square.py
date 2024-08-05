import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.floor(math.sqrt(num)) == math.ceil(math.sqrt(num))