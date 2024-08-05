class Solution:
    def digitCount(self, num_str) -> bool:
        memo = {}
        for i in range(0, len(num_str)):
            d = num_str[i]
            if (d in memo.keys()):
                memo[d] += 1
            else:
                memo[d] = 1
        
        my_num_str = ''
        for i in range(0, len(num_str)):
            if (str(i) in memo.keys()):
                my_num_str += str(memo[str(i)])
            else:
                my_num_str += '0'

        return my_num_str == num_str