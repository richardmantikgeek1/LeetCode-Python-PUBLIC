class Solution:
    def duplicateZeros(self, array):
        i = 0
        len_array = len(array)
        while (i < len(array)):
            if (array[i] == 0):
                array.insert(i, 0)
                array.pop(len_array)
                i += 1
            i += 1