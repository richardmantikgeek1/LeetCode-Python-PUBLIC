class Solution:
    def addBinary(self, a, b):
        sum_a_and_b = int(a, 2) + int(b, 2)
        return format(sum_a_and_b, 'b')