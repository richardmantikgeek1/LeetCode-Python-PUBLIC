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
    def minOperations(self, logs):
        stack = MyStack()
        i = 0
        while(i < len(logs)):
            log = logs[i]
            if (not stack.empty()):
                t = stack.top()
                if (log == '../'):
                    stack.pop()
                elif (log == './'):
                    pass
                else:
                    stack.push(log)
            else:
                stack.push(log)
            i += 1
        
        ret_val = stack.stack
        while (len(ret_val) > 0):
            if (ret_val[0] == '../' or ret_val[0] == './'):
                ret_val.popleft()
            else:
                break
        
        return len(ret_val)