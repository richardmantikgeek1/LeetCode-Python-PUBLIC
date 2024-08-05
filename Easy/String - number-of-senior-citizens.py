class Solution:
    def countSeniors(self, details):
        count_senior_citizens = 0
        for s in details:
            age = int(s[-4:-2])
            if (age > 60):
                count_senior_citizens += 1

        return count_senior_citizens