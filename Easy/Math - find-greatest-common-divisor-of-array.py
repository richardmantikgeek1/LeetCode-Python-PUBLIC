import math

class Solution:
    def findGCD(self, array):
        return math.gcd(min(array), max(array))