class Solution:
    def splitNum(self, num) -> int:
        digits = [int(c) for c in str(num)]
        digits = sorted(digits)
        nums = ['', '']
        i = 0
        step = 0
        while (i < len(digits)):
            d = digits[i]
            nums[step % 2] += str(d)
            step += 1
            i += 1

        ret_val = sum([int(n) for n in nums])
        return ret_val