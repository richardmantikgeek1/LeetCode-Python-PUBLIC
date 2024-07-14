class Solution:
    def isToeplitzMatrix(self, matrix):
        margin = 0
        i = 0
        j = 0
        last_num = None
        while (i < len(matrix)):
            j = i + margin
            if (j >= len(matrix[i])):
                break
            while (i < len(matrix) and j < len(matrix[i])):
                num = matrix[i][j]
                if (last_num is None):
                    last_num = num
                elif (last_num != num):
                    return False
                i += 1
                j += 1
            margin += 1
            i = 0
            j = 0
            last_num = None
        
        margin = 0
        i = 0
        j = 0
        last_num = None

        while (j < len(matrix[0])):
            i = j + margin
            if (i >= len(matrix)):
                break
            while (i < len(matrix) and j < len(matrix[i])):
                num = matrix[i][j]
                if (last_num is None):
                    last_num = num
                elif (last_num != num):
                    return False
                i += 1
                j += 1
            margin += 1
            i = 0
            j = 0
            last_num = None

        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
sol = Solution()
result = sol.isToeplitzMatrix(matrix)
print(result)