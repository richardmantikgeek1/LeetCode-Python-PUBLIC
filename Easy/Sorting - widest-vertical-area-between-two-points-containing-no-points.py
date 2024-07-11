class Solution:
    def maxWidthOfVerticalArea(self, points):
        ret_val = 0
        max_width = None
        x_coords = [x for x,y in points]
        x_coords = sorted(x_coords)
        for i in range(0, len(x_coords) - 1):
            x1 = x_coords[i]
            x2 = x_coords[i+1]
            if (max_width is None or x2-x1 > max_width):
                max_width = x2-x1

        return max_width