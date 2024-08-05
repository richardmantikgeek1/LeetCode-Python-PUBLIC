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

class MyQueue:

    def __init__(self):
        self.my_stack_1 = MyStack()
        self.my_stack_2 = MyStack()

    def push(self, x: int) -> None:
        self.my_stack_1.push(x)

    def pop(self) -> int:
        if (not self.my_stack_2.empty()):
            return self.my_stack_2.pop()
        else:
            while (not self.my_stack_1.empty()):
                self.my_stack_2.push(self.my_stack_1.pop())
                
            return self.my_stack_2.pop()

    def peek(self) -> int:
        if (not self.my_stack_2.empty()):
            return self.my_stack_2.top()
        else:
            while (not self.my_stack_1.empty()):
                self.my_stack_2.push(self.my_stack_1.pop())
            
            return self.my_stack_2.top()

    def empty(self) -> bool:
        return self.my_stack_1.empty() and self.my_stack_2.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()