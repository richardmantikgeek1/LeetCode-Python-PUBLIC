class Solution:
    def maximumValue(self, strs):
        values = []
        for s in strs:
            try:
                val = int(s)
            except ValueError:
                val = len(s)
            
            values.append(val)
        
        return max(values)
