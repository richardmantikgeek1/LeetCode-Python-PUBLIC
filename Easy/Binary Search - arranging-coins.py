from collections import deque
class Solution:
    def arrangeCoins(self, count_coins):
        count_squares = 0
        stairs_height = 1
        stairs_array = deque()
        while (count_squares <= count_coins):
            count_squares += stairs_height
            stairs_array.appendleft(stairs_height)
            stairs_height += 1

        for i in range(0, len(stairs_array)):
            stairs_height = stairs_array[i]
            if (count_squares >= stairs_height):
                count_squares -= stairs_height
            else:
                return i
        
        return i
    
sol = Solution()
result = sol.arrangeCoins(3)
print(result)