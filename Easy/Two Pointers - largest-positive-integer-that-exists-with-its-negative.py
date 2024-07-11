class Solution:
    def findMaxK(self, array):
        array = sorted(array)
        print(array)
        i = 0
        j = len(array) - 1
        memo = {}
        while (i < j):
            while (i < len(array)
                   and array[i] < 0
                   and -1 * array[i] >= array[j]):
                memo[array[i]] = True
                i += 1
            if (-1 * array[j] in memo.keys()):
                return array[j]

            j -= 1

        return -1

array = [-1,2,-3,3]
sol = Solution()
max_k = sol.findMaxK(array)
print(max_k)