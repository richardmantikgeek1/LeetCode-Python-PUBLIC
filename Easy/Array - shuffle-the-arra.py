class Solution:
    def shuffle(self, array, n):
        i = 0
        new_array = []
        while (i < len(array)):
            if (i % 2 == 0):
                new_array.append(array[i//2])
            else:
                new_array.append(array[(len(array)//2) + i//2])
            i += 1
        
        return new_array