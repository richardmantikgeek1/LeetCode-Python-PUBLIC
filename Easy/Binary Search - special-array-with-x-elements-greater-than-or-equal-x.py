class Solution:
    def specialArray(self, array):
        array = sorted(array)

        for x in range(0, len(array)+1):
            if (len(array) - self.binary_search_iterative(array, x) == x):
                return x
        
        return -1
    
    def binary_search_iterative(self, memo, target):
        start_index = 0
        end_index = len(memo) - 1
        while (start_index <= end_index):
            mid_index = (start_index + end_index) // 2
            if (mid_index == len(memo)-1 and target > memo[mid_index]):
                return mid_index + 1
            elif (target > memo[mid_index] and target <= memo[mid_index+1]):
                return mid_index + 1
            elif (target <= memo[mid_index]):
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        return 0
    
array = [0,0,3,4,4]
sol = Solution()
print(sol.binary_search_iterative(array, 3))
