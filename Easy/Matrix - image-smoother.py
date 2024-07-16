import math
import copy
class Solution:
    def imageSmoother(self, img):
        img_copy = copy.deepcopy(img)
        for i in range(0, len(img)):
            for j in range(0, len(img[i])):
                img_copy[i][j] = self.get_floor_avg_cell_and_sorrounding_cells(i, j, img)
        return img_copy
    
    def get_floor_avg_cell_and_sorrounding_cells(self, i, j, img):
        sum_cell_and_sorrounding_cells = 0
        count_cells = 0
        sum_cell_and_sorrounding_cells += img[i][j]
        count_cells += 1
        
        if (i - 1 >= 0 and j - 1 >= 0):
            sum_cell_and_sorrounding_cells += img[i-1][j-1]
            count_cells += 1
        
        if (i - 1 >= 0):
            sum_cell_and_sorrounding_cells += img[i-1][j]
            count_cells += 1

        if (i -1 >= 0 and j+1 < len(img[0])):
            sum_cell_and_sorrounding_cells += img[i-1][j+1]
            count_cells += 1
        
        if (j - 1 >= 0):
            sum_cell_and_sorrounding_cells += img[i][j-1]
            count_cells += 1

        if (j+1 < len(img[0])):
            sum_cell_and_sorrounding_cells += img[i][j+1]
            count_cells += 1
        
        if (i + 1 < len(img) and j - 1 >= 0):
            sum_cell_and_sorrounding_cells += img[i+1][j-1]
            count_cells += 1
        
        if (i + 1 < len(img)):
            sum_cell_and_sorrounding_cells += img[i+1][j]
            count_cells += 1
        
        if (i + 1 < len(img) and j + 1 < len(img[0])):
            sum_cell_and_sorrounding_cells += img[i+1][j+1]
            count_cells += 1

        return math.floor(sum_cell_and_sorrounding_cells/count_cells)

img = [[100,200,100],[200,50,200],[100,200,100]]
sol = Solution()
result = sol.get_floor_avg_cell_and_sorrounding_cells(1,2,img)
print(result)