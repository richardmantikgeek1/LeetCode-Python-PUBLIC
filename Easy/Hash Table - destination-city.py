class Solution:
    def destCity(self, paths):
        map = {}
        #map['from_city_1'] = 'to_city_2'
        #map['from_city_2'] = 'to_city_3'
        for path in paths:
            map[path[0]] = path[1]
        
        start_city = None
        for k in map.keys():
            if (k not in map.values()):
                start_city = k
                break
        
        dest_cities = []
        for k in map.keys():
            dest_cities.append(map[start_city])
            start_city = map[start_city]
        
        return dest_cities[len(dest_cities) - 1]