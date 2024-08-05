from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if (not self.empty()):
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if (not self.empty()):
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def empty(self) -> bool:
        return len(self.stack) == 0

class Solution:
    def backspaceCompare(self, s, t):
        print(self.get_backspaced_str(s) )
        print(self.get_backspaced_str(t) )
        
        return self.get_backspaced_str(s) == self.get_backspaced_str(t)

    def get_backspaced_str(self, s):
        stack = MyStack()
        i = 0
        while (i < len(s)):
            c = s[i]
            if (not stack.empty()):
                t = stack.top()
                if (c == '#'):
                    stack.pop()
                else:
                    stack.push(c)
            else:
                stack.push(c)
            i += 1
        
        ret_val = ''.join(stack.stack)
        
        i = 0
        while (i < len(ret_val)):
            if (ret_val[i] != '#'):
                break
            i += 1
            
        return ret_val[i:]