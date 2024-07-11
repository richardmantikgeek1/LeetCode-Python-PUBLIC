class Solution:
    def findRelativeRanks(self, scores):
        rs_scores = sorted(scores, reverse=True)
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        map = {}
        i = 0
        while (i < min(len(rs_scores), len(ranks))):
            map[rs_scores[i]] = ranks[i]
            i += 1
        
        while (i < max(len(rs_scores), len(ranks))):
            if (i >= len(rs_scores)):
                break
            map[rs_scores[i]] = str(i + 1)
            i += 1
        

        ret_val = [map[s] for s in scores]
        return ret_val