class Solution:
    def busyStudent(self, start_time, end_time, query_time):
        ret_val = 0
        for i in range(0, len(start_time)):
            s = start_time[i]
            e = end_time[i]
            if (s <= query_time <= e):
                ret_val += 1

        return ret_val

