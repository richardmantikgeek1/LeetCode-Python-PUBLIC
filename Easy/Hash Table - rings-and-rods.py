class Solution:
    def countPoints(self, rings):
        start_index = 0
        memo = {}
        while (start_index < len(rings)):
            ring = rings[start_index]
            rod = rings[start_index + 1]

            if (rod in memo.keys()):
                if (ring in memo[rod].keys()):
                    memo[rod][ring] += 1
                else:
                    memo[rod][ring] = 1
            else:
                memo[rod] = {ring: 1}

            start_index += 2

        ret_val = 0
        for rod in memo.keys():
            if (len(memo[rod].keys()) == 3):
                ret_val += 1

        return ret_val