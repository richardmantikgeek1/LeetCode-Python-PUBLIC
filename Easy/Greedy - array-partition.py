class Solution:
    def arrayPairSum(self, array):
        #combs = [(i,j) for i in range(0, len(array)) for j in range(0, len(array)) if i != j]
        #uniq_combs = []
        #a_map = {}
        #for i, j in combs:
        #    key = ' '.join([str(a) for a in sorted([i, j])])
        #    a_map[key] = True

        #index_pairs = []
        #for k in a_map.keys():
        #    ij_pair_0 = k.split(' ')
        #    i = int(ij_pair_0[0])
        #    j = int(ij_pair_0[1])
        #    index_pairs.append((i,j))
        
        sorted_array = sorted(array)
        max_sum_min_pair = 0
        num_pairs = []
        for i in range(0, len(sorted_array)-1, 2):
            j = i + 1
            num_pairs.append((sorted_array[i], sorted_array[j]))
            max_sum_min_pair += min(sorted_array[i], sorted_array[j])
        
        return max_sum_min_pair



            
            
array = [1,4,3,2]
sol = Solution()
print(sol.arrayPairSum(array))