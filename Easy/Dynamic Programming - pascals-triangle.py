import time

class Solution:
    def getRow(self, rowIndex):
        pascal_triangle = self.generate(rowIndex+1)
        return pascal_triangle[rowIndex]

    def generate(self, numRows): # using Dynamic Programming
        ret_val = [[1]]
        for i in range(1, numRows): # O(N) * O(N) => O(N^2)
            curr_pascal_line = ret_val[i-1]
            ret_val.append(self.next_pascal_line(curr_pascal_line))
        
        return ret_val


    def generate_1(self, numRows):
        ret_val = []
        for i in range(0, numRows): # O(N) * O(N*N) => O(N^3) => Tracktable Problem
            ret_val.append(self.pascal_line(i))
        
        return ret_val

    def pascal_line(self, i): # time_complexity: O(N) * (time_complexity of self.pascal_line(i-1))
                              #                  O(N) * (O(N) * time_complexity of self.pascal_line(i-2))
                              #                  O(N*N)
        if (i == 0):
            return [1]
        elif (i > 0):
            prev_pascal_line = self.pascal_line(i-1)
            curr_pascal_line = []
            for j in range(0, len(prev_pascal_line)):
                if (j == 0):
                    curr_pascal_line.append(prev_pascal_line[j])
                elif (j > 0):
                    curr_pascal_line.append(prev_pascal_line[j] + prev_pascal_line[j-1])
            curr_pascal_line.append(1)

            return curr_pascal_line
    
    def next_pascal_line(self, curr_pascal_line): # O(N)
        next_pascal_line = []
        for j in range(0, len(curr_pascal_line)): # O(N)
            if (j == 0):
                next_pascal_line.append(curr_pascal_line[j]) # O(N)
            elif (j > 0):
                next_pascal_line.append(curr_pascal_line[j] + curr_pascal_line[j-1]) # O(2) => O(1)
        next_pascal_line.append(1)

        return next_pascal_line

start_time = time.time()
sol = Solution()
#print(sol.pascal_line(4))
print(sol.generate_1(10))
end_time = time.time()
print("The time of execution of above program is :", (end_time-start_time) * 10**3, "ms") 