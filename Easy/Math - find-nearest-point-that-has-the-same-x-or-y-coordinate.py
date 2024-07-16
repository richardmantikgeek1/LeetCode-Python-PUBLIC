class Solution:
    def nearestValidPoint(self, x, y, points) -> int:
        shared_coord_points = [p for p in points if p[0] == x or p[1] == y]
        memo = {}
        for i in range(0, len(shared_coord_points)):
            point = shared_coord_points[i]
            manhattan_dist = abs(point[0] - x) + abs(point[1] - y)
            if (manhattan_dist not in memo.keys()):
                memo[manhattan_dist] = point

        for key in sorted(memo.keys()):
            point = memo[key]
            return points.index(point)
            
        return -1

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
sol = Solution()
result = sol.nearestValidPoint(x, y, points)
print(result)