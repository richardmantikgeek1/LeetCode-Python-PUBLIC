from collections import deque
class Person:
    def __init__(self, initial_pos, count_tickets_to_buy):
        self.initial_pos = initial_pos
        self.count_tickets_to_buy = count_tickets_to_buy
    def __str__(self):
        return ('person k = ' + str(self.initial_pos) + ', count_tickets_to_buy = ' + str(self.count_tickets_to_buy))

class Solution:
    def timeRequiredToBuy(self, array, k):
        queue = deque()
        for i in range(0, len(array)):
            count_tickets_to_buy = array[i]
            p = Person(i, count_tickets_to_buy)
            queue.append(p)
        
        time_to_finish_buying_tickets = 0
        while (len(queue) > 0):
            p = queue.popleft()
            p.count_tickets_to_buy -= 1
            time_to_finish_buying_tickets += 1
            if (p.count_tickets_to_buy == 0 and p.initial_pos == k):
                return time_to_finish_buying_tickets
            if (p.count_tickets_to_buy > 0):
                queue.append(p)
        
        
        return -1