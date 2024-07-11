class Solution:
    def countMatches(self, items, rule_key, rule_value):
        map_array = []
        for item in items:
            map = {}
            map['type']     = item[0]
            map['color']    = item[1]
            map['name']     = item[2]
            map_array.append(map)
        
        count_matches = 0
        for map in map_array:
            if map[rule_key] == rule_value:
                count_matches += 1

        return count_matches