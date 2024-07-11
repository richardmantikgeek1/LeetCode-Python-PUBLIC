#User function Template for python3

class Solution:
    def runningSum(self, array):
        prefix_sum = 0
        running_sum = []

        for i in range(0, len(array)):
            num = array[i]

            prefix_sum += num
            running_sum.append(prefix_sum)
            
        
        return running_sum