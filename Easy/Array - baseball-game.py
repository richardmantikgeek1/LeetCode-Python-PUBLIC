from collections import deque

class Solution:
    def calPoints(self, operations):
        queue = deque()
        for op in operations:
            if (op == 'C'):
                queue.pop()
            elif (op == 'D'):
                last_num = queue[len(queue) - 1]
                queue.append(last_num * 2)
            elif (op == '+'):
                last_num = queue[len(queue) - 1]
                prev_last_num = queue[len(queue) - 2]
                queue.append(last_num + prev_last_num)
            else:
                queue.append(int(op))
    
            print(queue)
        return sum(queue)