class Solution:
    def countSeniors(self, details):
        ret_val = 0
        for d in details:
            if (int(d[11:13]) > 60):
                ret_val += 1
        
        return ret_val