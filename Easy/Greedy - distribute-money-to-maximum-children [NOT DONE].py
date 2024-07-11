class Solution:
    def distMoney(self, money, children):
        if (money < children):
            return -1

        remaining_money = money
        ret_val = 0
        while (remaining_money > 4 + 8 or (remaining_money > 0 and remaining_money%8 == 0 and money/8 >= children)):
            remaining_money -= 8
            ret_val += 1

        if (remaining_money % 8 == 4 and children - ret_val == 2):
            remaining_money -= 3
        elif (remaining_money > 8):
            remaining_money -= 8
            ret_val += 1
        ret_val = self.count_children_receives_8_dollars(money, children, ret_val)
        if (remaining_money < (children-ret_val)):
            return 0

        return ret_val
    
    def count_children_receives_8_dollars(self, money, children, ret_val):
        if (ret_val == children and money - ret_val * 8 < 8 and money - ret_val * 8 > 0):
            return ret_val - 1
        else:
            return ret_val
