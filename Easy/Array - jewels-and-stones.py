class Solution:
    def numJewelsInStones(self, jewels, stones) -> int:
        jewels = [str(c) for c in jewels]
        jewels_map = {}
        i = 0
        while (i < len(jewels)):
            jewel = jewels[i]
            jewels_map[jewel] = True
            i += 1
        
        ret_val = 0
        i = 0
        while (i < len(stones)):
            stone = stones[i]
            if (stone in jewels_map.keys()):
                ret_val += 1
            i += 1
        return ret_val