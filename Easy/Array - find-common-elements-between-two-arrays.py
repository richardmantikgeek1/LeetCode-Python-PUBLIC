class Solution:
    def findIntersectionValues(self, nums_1, nums_2):
        answer_1 = 0
        for i in range(0, len(nums_1)):
            num_1 = nums_1[i]
            try:
                j = nums_2.index(num_1)
                answer_1 += 1
            except:
                pass
        
        answer_2 = 0
        for i in range(0, len(nums_2)):
            num_2 = nums_2[i]
            try:
                j = nums_1.index(num_2)
                answer_2 += 1
            except:
                pass
        
        return [answer_1, answer_2]