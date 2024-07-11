class Solution:
    def minMovesToSeat(self, seats, students):
        seats = sorted(seats)
        students = sorted(students)
        ret_val = 0
        for i in range(0, len(seats)):
            ret_val += abs(seats[i]-students[i])
            
        return ret_val