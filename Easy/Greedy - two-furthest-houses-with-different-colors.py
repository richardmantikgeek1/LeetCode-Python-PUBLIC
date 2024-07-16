class Solution:
    def maxDistance(self, colors):
        memo = {}
        for i in range(0, len(colors)):
            color = colors[i]
            if (color in memo.keys()):
                memo[color].append(i)
            else:
                memo[color] = [i]

        max_distance = None
        for color_1 in memo.keys():
            for color_2 in memo.keys():
                if (color_1 != color_2):
                    i1 = min(memo[color_1])
                    i2 = max(memo[color_2])
                    if (max_distance is None or max_distance < abs(i2 - i1)):
                        max_distance = abs(i2 - i1)
        
        return max_distance