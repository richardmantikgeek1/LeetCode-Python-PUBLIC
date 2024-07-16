class Solution:
    def findTheDistanceValue(self, array_1, array_2, d):
        array_1 = sorted(array_1)
        array_2 = sorted(array_2)
        ret_val = 0
        for i in range(0, len(array_1)):
            num_1 = array_1[i]
            is_distanced = True
            for j in range(0, len(array_2)):
                num_2 = array_2[j]
                if (abs(num_1 - num_2) <= d):
                    is_distanced = False
                    break
            if (is_distanced):
                ret_val += 1
        return ret_val