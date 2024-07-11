class Solution:
    def shortestToChar(self, s, c):
        i = 0
        c_positions = []
        while (i < len(s)):
            if (s[i] == c):
                c_positions.append(i)
            i+= 1
        
        ret_val = []
        i = 0    
        while (i < len(s)):
            ret_val.append(self.closest_index(i, c_positions))
            i+=1
        return ret_val

    def closest_index(self, index, indices):
        min_index_dist_i = None
        min_index_dist = None
        for i in range(0, len(indices)):
            index_dist = abs(indices[i] - index)
            if (min_index_dist is None or min_index_dist > index_dist):
                min_index_dist_i = i
                min_index_dist = index_dist
        
        return min_index_dist

sol = Solution()
print(sol.shortestToChar('loveleetcode', 'e'))
