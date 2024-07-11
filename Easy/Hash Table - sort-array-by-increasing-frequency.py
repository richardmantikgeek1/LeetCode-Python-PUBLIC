class Solution:
    def frequencySort(self, array):
        num_freq_map = {}
        for num in array:
            if (num in num_freq_map.keys()):
                num_freq_map[num] += 1
            else:
                num_freq_map[num] = 1

        freq_nums_map = {}
        for num in num_freq_map.keys():
            freq = num_freq_map[num]
            if (freq in freq_nums_map.keys()):
                freq_nums_map[freq].append(num)
            else:
                freq_nums_map[freq] = [num]
        
        ret_val = []
        for freq in sorted(freq_nums_map.keys()):
            nums = freq_nums_map[freq]
            for num in reversed(sorted(nums)):
                ret_val.extend([num] * freq)
        
        return ret_val