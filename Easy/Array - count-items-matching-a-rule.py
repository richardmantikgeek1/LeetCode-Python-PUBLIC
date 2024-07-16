class Solution:
    def countMatches(self, items, rule_key, rule_value):
        array = []
        for item in items:
            item_map = {}
            item_map['type'] = item[0]
            item_map['color'] = item[1]
            item_map['name'] = item[2]
            array.append(item_map)
            
        return len([a for a in array if a[rule_key] == rule_value])