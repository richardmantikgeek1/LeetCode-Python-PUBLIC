import math

class Solution:
    def pickGifts(self, gifts, k):
        while (k > 0):
            max_num_value = max(gifts)
            max_num_index = gifts.index(max_num_value)
            gifts[max_num_index] = math.floor(math.sqrt(max_num_value))
            k -= 1
        
        return sum(gifts)
        