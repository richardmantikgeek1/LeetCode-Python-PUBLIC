class Solution:
    def maximum69Number (self, num):
        num_str = str(num)
        i = 0
        while(i < len(num_str)):
            c = num_str[i]
            if (c == '6'):
                num_str = num_str[:i] + '9' + num_str[i+1:]
                break
            i+=1

        return int(num_str)
    
sol = Solution()
print(sol.maximum69Number(9669))