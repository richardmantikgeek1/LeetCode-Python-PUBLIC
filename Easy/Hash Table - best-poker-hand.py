from collections import defaultdict
class Solution:
    def bestHand(self, ranks, suits):
        suits_map = defaultdict(int)
        for s in suits:
            suits_map[s] += 1
        ranks_map = defaultdict(int)
        for r in ranks:
            ranks_map[r] += 1
        if (len(suits_map) == 1):
            return 'Flush'
        elif(len([ranks_map[r] for r in ranks_map.keys() if ranks_map[r] >= 3]) > 0):
            return 'Three of a Kind'
        elif(len([ranks_map[r] for r in ranks_map.keys() if ranks_map[r] == 2]) > 0):
            return 'Pair'
        else:
            return 'High Card'