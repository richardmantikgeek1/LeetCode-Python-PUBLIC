class Solution:
    def maxScore(self, s):
        inv_s = self.inverse_str(s)
        inv_array = [int(c) for c in inv_s]
        array = [int(c) for c in s]
        left_sum    = deque()
        right_sum   = deque()
        prefix_sum  = 0

        for i in range(0, len(inv_array)):
            num = inv_array[i]

            left_sum.append(prefix_sum)
            prefix_sum += num
        left_sum.append(prefix_sum)

        prefix_sum = 0
        for i in range(len(array) - 1, -1, -1):
            num = array[i]

            right_sum.appendleft(prefix_sum)
            prefix_sum += num
        right_sum.appendleft(prefix_sum)

        max_score = 0
        for i in range(1, len(left_sum)-1):
            max_score = max(max_score, left_sum[i] + right_sum[i])
        
        return max_score

    def inverse_str(self, s):
        i = 0
        ret_val = ''
        while (i < len(s)):
            c = s[i]
            if (c == '0'):
                ret_val += '1'
            else:
                ret_val += '0'
            i+= 1

        return ret_val