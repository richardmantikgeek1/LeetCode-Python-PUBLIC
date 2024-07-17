class Solution:
    def intersect(self, array_1, array_2):
        memo_1 = {}
        for i in range(0, len(array_1)):
            num_1 = array_1[i]

            if (num_1 in memo_1.keys()):
                memo_1[num_1] += 1
            else:
                memo_1[num_1] = 1
        
        memo_2 = {}
        for j in range(0, len(array_2)):
            num_2 = array_2[j]

            if (num_2 in memo_2.keys()):
                memo_2[num_2] += 1
            else:
                memo_2[num_2] = 1

        ret_val = []
        for num in memo_1.keys():
            num_1_freq = None
            if (num in memo_1.keys()):
                num_1_freq = memo_1[num]
            else:
                num_1_freq = 0

            num_2_freq = None
            if (num in memo_2.keys()):
                num_2_freq = memo_2[num]
            else:
                num_2_freq = 0
        
            ret_val.extend([num] * min(num_1_freq, num_2_freq))
    
        return ret_val
