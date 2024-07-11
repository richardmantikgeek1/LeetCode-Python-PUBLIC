class Solution:
    def maxFrequencyElements(self, array):
        freq_map = {}
        #freq_map[1] = 2
        #freq_map[2] = 2
        #freq_map[3] = 1
        #freq_map[4] = 1

        for i in range(0, len(array)):
            num = array[i]
            if (num in freq_map.keys()):
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        memo = {}
        # memo[num_freq] = [num_1, num_2]
        for num in freq_map:
            freq = freq_map[num]
            if (freq in memo.keys()):
                memo[freq].append(num)
            else:
                memo[freq] = [num]

        max_freq = max(list(memo.keys()))
        
        ret_val = 0
        for k in freq_map.keys():
            if (max_freq == freq_map[k]):
                ret_val += freq_map[k]
        
        return ret_val