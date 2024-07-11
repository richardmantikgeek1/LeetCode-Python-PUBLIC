class Solution_a:
    def getCommon(self, array_1, array_2):
        set_1 = set(array_1)
        set_2 = set(array_2)
        intersection_set = set_1.intersection(set_2)
        if (len(intersection_set) > 0):
            return min(intersection_set)
        else:
            return -1
        
class Solution:
    def getCommon(self, array_1, array_2):
        memo = {}
        intersection = []
        for i in range(0, len(array_1)):
            num_i = array_1[i]
            memo[num_i] = True

        for j in range(0, len(array_2)):
            num_j = array_2[j]
            if (num_j in memo.keys()):
                intersection.append(num_j)

        if (len(intersection) > 0):
            return min(intersection)
        else:
            return -1
