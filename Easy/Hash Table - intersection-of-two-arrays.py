class Solution:
    def intersection(self, array_1, array_2):
        memo = {}
        ret_val = []

        for i in range(0, len(array_1)):
            num_1 = array_1[i]
            memo[num_1] = True

        for i in range(0, len(array_2)):
            num_2 = array_2[i]
            if (num_2 in memo.keys() and num_2 not in ret_val):
                ret_val.append(num_2)
        
        return ret_val