class Solution:
    def arithmeticTriplets(self, array, diff):
        ret_val = 0
        memo = {}
        for i in range(0, len(array)):
            num_i = array[i]
            num_j = num_i + diff
            memo[num_j] = i
        
        indexof = {}
        for j in range(0, len(array)):
            num_j = array[j]
            if (num_j in indexof.keys()):
                indexof[num_j].append(j)
            else:
                indexof[num_j] = [j]

        for k in range(0, len(array)):
            num_k = array[k]
            num_j = num_k - diff
            if (num_j in memo.keys() and memo[num_j] < k):
                i = memo[num_j]
                try:
                    js = indexof[num_j]
                    for j in js:
                        if (i < j and j < k):
                            ret_val += 1
                except:
                    pass
                    
        return ret_val
array = [0,1,4,6,7,10]
diff = 3
sol = Solution()
print(sol.arithmeticTriplets(array, diff))