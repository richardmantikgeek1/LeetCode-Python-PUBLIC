from collections import defaultdict
class Solution:
    def countQuadruplets(self, array):
        memo = defaultdict(list)
        ret_val = 0

        # num_a + num_b + num_c == num_d
        # num_a + num_b == num_d - num_c
        for c in range(0, len(array)):
            num_c = array[c]
            for d in range(c+1, len(array)):
                num_d = array[d]
                num_a_plus_num_b = num_d - num_c
                memo[num_a_plus_num_b].append(c)

        for a in range(0, len(array)):
            num_a = array[a]
            for b in range(a+1, len(array)):
                num_b = array[b]
                num_a_plus_num_b = num_a + num_b
                if (num_a_plus_num_b in memo.keys()):
                    cs = memo[num_a_plus_num_b]
                    for c in cs:
                        if (c > b):
                            ret_val += 1

        return ret_val