class Solution:
    def defangIPaddr(self, address):
        ret_val = ''
        i = 0
        while (i < len(address)):
            c = address[i]
            if (c == '.'):
                c = '[.]'
            ret_val += c
            i += 1

        return ret_val