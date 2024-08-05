class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count_steps = 0
        while (amount != [0,0,0]):
            max_amount = max(amount)
            max_amount_i = amount.index(max_amount)
            the_rest = amount[:max_amount_i] + amount[max_amount_i + 1:]
            second_max_amount = max(the_rest)
            second_max_amount_i = amount.index(second_max_amount)
            if (max_amount == second_max_amount):
                j = max_amount_i + 1
                while (j < len(amount)):
                    if (amount[j] == second_max_amount):
                        break
                    j+=1
                second_max_amount_i = j
            
            if (max_amount > 0 and second_max_amount > 0):
                amount[max_amount_i] -= 1
                amount[second_max_amount_i] -= 1
            else:
                amount[max_amount_i] -= 1
            
            count_steps += 1
    
        return count_steps