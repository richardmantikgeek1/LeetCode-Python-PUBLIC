class Solution:
    def isPathCrossing(self, path: str) -> bool:
        memo = {}
        coord = [0, 0]
        coord_str = '(' + str(coord[0]) + ',' + str(coord [1]) + ')'
        memo[coord_str] = True
        for i in range(0, len(path)):
            p = path[i]
            if (p == 'N'):
                coord = [coord[0], coord[1] + 1]
            elif (p == 'E'):
                coord = [coord[0]+1, coord[1]]
            elif (p == 'S'):
                coord = [coord[0], coord[1] - 1]
            elif (p == 'W'):
                coord = [coord[0]-1, coord[1]]

            coord_str = '(' + str(coord[0]) + ',' + str(coord [1]) + ')'
            if (coord_str in memo.keys()):
                return True
            memo[coord_str] = True

        return False
    
sol = Solution()
result = sol.isPathCrossing('NESWW')
print(result)