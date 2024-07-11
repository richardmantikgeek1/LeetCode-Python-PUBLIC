class Solution:
    def smallestEqual(self, array):
        for i in range(0, len(array)):
            num = array[i]
            if (i % 10 == num):
                return i
            
        return -1