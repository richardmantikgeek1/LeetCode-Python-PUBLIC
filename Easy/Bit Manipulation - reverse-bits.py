class Solution:
    def reverseBits(self, n):
        binary_num = format(n, 'b').zfill(32)
        
        return int(binary_num[::-1], 2)