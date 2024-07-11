class Solution:
    def subsetXORSum(self, array):
        combs = self.my_combine(array)
        ret_val = 0
        for comb in combs:
            ret_val += self.xor_array(comb)
        return ret_val

    def my_combine(self, array):
        if (array == []):
            return [[]]
        
        head = array[0:1]
        the_rest = array[1:]
        ret_val = self.my_combine(the_rest)
        
        ret_val = [head + rv for rv in ret_val] + ret_val
        return ret_val
    
    def xor_array(self, array):
        if (len(array) == 0): return 0

        max_len_s = max([len(format(a, 'b')) for a in array])
        ret_val = None
        for i in range(0, len(array)):
            num = array[i]
            num_b = format(num, 'b').zfill(max_len_s)
            if (ret_val is None):
                ret_val = num_b
            else:
                ret_val = self.xor_string(ret_val, num_b)
        
        if (ret_val is not None):
            return int(str(ret_val), 2)
        else:
            return 0
    
    def xor_string(self, s1, s2):
        ret_val = ''
        for i in range(0, len(s1)):
            if (s1[i] == s2[i]):
                ret_val += '0'
            else:
                ret_val += '1'
        return ret_val

sol = Solution()
print(sol.subsetXORSum([3,4,5,6,7,8]))