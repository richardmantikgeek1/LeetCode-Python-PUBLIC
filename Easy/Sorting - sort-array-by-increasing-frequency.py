class Solution:
    def frequencySort(self, array):
        num_to_freq_map = {}
        for i in range(0, len(array)):
            num = array[i]
            if (num in num_to_freq_map.keys()):
                num_to_freq_map[num] += 1
            else:
                num_to_freq_map[num] = 1

        freq_to_nums_map = {}
        for num in reversed(sorted(num_to_freq_map.keys())):
            freq = num_to_freq_map[num]
            if (freq in freq_to_nums_map.keys()):
                freq_to_nums_map[freq].append(num)
            else:
                freq_to_nums_map[freq] = [num]

        ret_val = []
        for freq in sorted(freq_to_nums_map.keys()):
            nums = freq_to_nums_map[freq]
            for num in nums:
                ret_val.extend([num] * freq)
    
        return ret_val