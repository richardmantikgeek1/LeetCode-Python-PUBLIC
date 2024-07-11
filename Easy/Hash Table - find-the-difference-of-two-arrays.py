class Solution:
    def findDifference(self, nums_1, nums_2):
        memo_nums_1 = {}
        for num_1 in nums_1:
            memo_nums_1[num_1] = True

        memo_nums_2 = {}
        for num_2 in nums_2:
            memo_nums_2[num_2] = True
        
        answer_0 = []
        for k in memo_nums_1.keys():
            if (k not in memo_nums_2.keys()):
                answer_0.append(k)

        answer_1 = []
        for k in memo_nums_2.keys():
            if (k not in memo_nums_1.keys()):
                answer_1.append(k)

        return [answer_0, answer_1]