class Solution:
    def countLargestGroup(self, n):
        groups = {}
        for num in range(1, n+1):
            num_str = str(num)
            sum_digits = sum([int(d) for d in str(num)])
            if (sum_digits in groups.keys()):
                groups[sum_digits] += 1
            else:
                groups[sum_digits] = 1
        
        freq_to_sum_digits_map = {}
        for sum_digits in groups.keys():
            freq = groups[sum_digits]
            if (freq in freq_to_sum_digits_map.keys()):
                freq_to_sum_digits_map[freq].append(sum_digits)
            else:
                freq_to_sum_digits_map[freq] = [sum_digits]
        
        for freq in reversed(sorted(freq_to_sum_digits_map.keys())):
            return len(freq_to_sum_digits_map[freq])

