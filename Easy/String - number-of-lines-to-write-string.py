class Solution:
    def numberOfLines(self, widths, s):
        memo = {}
        for i in range(0, len(widths)):
            width = widths[i]
            memo[chr(97+i)] = width

        count_lines = 0
        sum_pixel_width = 0
        last_i = 0
        for i in range(0, len(s)):
            c = s[i]
            if (sum_pixel_width + memo[c] > 100):
                count_lines += 1
                sum_pixel_width = memo[c]
                last_i = i
            else:
                sum_pixel_width += memo[c]

        i = last_i
        count_lines += 1
        sum_pixel_width = 0
        while (i < len(s)):
            c = s[i]
            sum_pixel_width += memo[c]
            i += 1

        return (count_lines, sum_pixel_width)


widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = 'bbbcccdddaaa'
sol = Solution()
result = sol.numberOfLines(widths, s)
print(result)        