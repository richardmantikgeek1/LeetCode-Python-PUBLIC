class Solution:
    def removeDuplicates(self, s):
        i = 0
        array = [c for c in s]
        while (i < len(array)-1):
            if (array[i] == array[i+1]):
                array.pop(i+1)
                array.pop(i)
                i -= 1
                if (i < 0):
                    i = 0
            else:
                i += 1
        return ''.join(array)