class Solution:
    def longestCommonPrefix(self, array):
        start_index = 0
        str_0 = array[0]
        common_prefix = ''
        while (start_index < len(str_0)):
            c = str_0[start_index]
            for i in range(0, len(array)):
                str_i = array[i]
                if (not str_i.startswith(common_prefix+c)):
                    return common_prefix

            common_prefix += c
            start_index += 1
        
        return common_prefix
    
sol = Solution()
array = ["flower","flow","flight"]
print(sol.longestCommonPrefix(array))