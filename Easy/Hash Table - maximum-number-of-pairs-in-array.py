class Solution:
    def numberOfPairs(self, array):
        map = {}
        i = 0
        while(i < len(array)):
            num = array[i]
            
            if (num in map.keys()):
                map[num].append(i)
            else:
                map[num] = [i]
            
            i += 1

        count_pairs_formed = 0
        for num in reversed(map.keys()):
            num_indices = list(reversed(map[num]))
            j = len(num_indices) - 1
            while (j >= 0):
                if (j - 1 < 0):
                    break
                num_indices.pop(j)
                num_indices.pop(j-1)
                count_pairs_formed += 1
                j -= 2
            
        return [count_pairs_formed, len(array)-count_pairs_formed * 2]

array = [1,3,2,1,3,2,2]
sol = Solution()
ret_val = sol.numberOfPairs(array)
print(ret_val)