class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ret_val = 0
        for num in nums:
            ret_val += self.encrypt(num)
        return ret_val

    def encrypt(self, num):
        num_str = str(num)
        max_digit = max([int(d) for d in num_str])
        return int(len(num_str) * str(max_digit))