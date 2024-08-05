class Solution:
    def readBinaryWatch(self, turnedOn):
        start_watch = '0000000000'
        end_watch   = '1111111111'

        ret_val = []

        for w in range(int(start_watch, 2), int(end_watch, 2)+1):
            b = format(w, 'b').zfill(len(start_watch))
            if (b.count('1') == turnedOn):
                h_m = self.mask(b)
                if (h_m[0] < 12 and h_m[1] < 60):
                    ret_val.append(str(h_m[0]) + ':' + str(h_m[1]).zfill(2))
        
        return ret_val
            
    def mask(self, b):
        h_b = b[0:4]
        m_b = b[4:]
        h = sum([2**(len(h_b)-i-1) for i in range(0, len(h_b)) if h_b[i] == '1'])
        m = sum([2**(len(m_b)-i-1) for i in range(0, len(m_b)) if m_b[i] == '1'])
        return h, m

sol = Solution()
print(sol.readBinaryWatch(1))
print(sol.mask('1001110000'))

        