class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return len([h for h in hours if h >= target])