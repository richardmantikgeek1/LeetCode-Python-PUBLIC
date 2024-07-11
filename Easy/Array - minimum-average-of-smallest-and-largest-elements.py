class Solution:
    def minimumAverage(self, array):
        averages = []
        while (len(array) > 0):
            min_num = min(array)
            min_num_index = array.index(min_num)
            array.pop(min_num_index)
            max_num = max(array)
            max_num_index = array.index(max_num)
            array.pop(max_num_index)
            averages.append((min_num + max_num) / 2)
        return min(averages)

sol = Solution()
print(sol.minimumAverage([7,8,3,4,15,13,4,1]))