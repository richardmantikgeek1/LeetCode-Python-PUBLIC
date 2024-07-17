from heapq import _heapify_max, _heappop_max, _siftdown_max

class Solution:
    def lastStoneWeight(self, stones):
        _heapify_max(stones)
        while (len(stones) > 1):
            first_heaviest_stone =  _heappop_max(stones)
            second_heaviest_stone = _heappop_max(stones)
            diff_2_heaviest_stones = abs(first_heaviest_stone - second_heaviest_stone)
            stones.append(diff_2_heaviest_stones)
        
        if (len(stones) == 1):
            return stones[0]
        else:
            return 0