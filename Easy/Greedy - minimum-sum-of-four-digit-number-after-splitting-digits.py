class Solution:
    def minimumSum(self, num):
        num_str = str(num)
        sorted_num_str = sorted(num_str)
        array = ['', '']
        i = 0
        while (i < len(sorted_num_str)):
            array[i % len(array)] += sorted_num_str[i]
            i += 1

        return sum([int(ns) for ns in array])

sol = Solution()
print(sol.minimumSum('2932'))