class Solution:
    def threeConsecutiveOdds(self, array):
        i = 0
        while (i < len(array)-2):
            num_1 = array[i]
            num_2 = array[i+1]
            num_3 = array[i+2]
            if (num_1 % 2 == 1
                and num_2 % 2 == 1
                and num_3 % 2 == 1):
                return True
            i += 1

        return False
