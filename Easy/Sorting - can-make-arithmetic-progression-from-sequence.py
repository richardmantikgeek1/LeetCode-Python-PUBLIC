class Solution:
    def canMakeArithmeticProgression(self, array):
        array = sorted(array)
        d = None
        for i in range(0, len(array) - 1):
            curr_d = array[i+1] - array[i]
            if (d is not None and curr_d != d):
                return False
            d = curr_d

        return True