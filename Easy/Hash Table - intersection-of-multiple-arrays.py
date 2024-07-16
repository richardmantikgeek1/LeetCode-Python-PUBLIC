class Solution:
    def intersection(self, array):
        intersection_set = set(array[0])
        i = 1
        while (i < len(array)):
            intersection_set = intersection_set.intersection(set(array[i]))
            i += 1
        
        return sorted(list(intersection_set))