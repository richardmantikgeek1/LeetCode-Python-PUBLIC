from functools import cmp_to_key

class Solution:
    def maximumUnits(self, box_types, truck_size) -> int:
        box_types = sorted(box_types, key=cmp_to_key(self.my_compare), reverse=True)
        truck_remaining_space = truck_size
        i = 0
        ret_val = 0
        for i in range(0, len(box_types)):
            box_type = box_types[i]
            if (truck_remaining_space >= box_type[0]):
                truck_remaining_space -= box_type[0]
                ret_val += box_type[0] * box_type[1]
            else:
                ret_val += truck_remaining_space * box_type[1]
                break

        return ret_val
    
    def my_compare (self, box_type_1, box_type_2):
        if box_type_1[1] < box_type_2[1]:
            return -1
        else:
            return 1
    
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
sol = Solution()
print(sol.maximumUnits(boxTypes, truckSize))