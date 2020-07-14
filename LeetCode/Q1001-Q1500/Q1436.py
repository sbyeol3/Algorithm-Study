class Solution:
    def destCity(self, paths) -> str:
        desCities = []
        for cities in paths :
            desCities.append(cities[1])
        for cities in paths :
            if cities[0] in desCities :
                desCities.remove(cities[0])
        return desCities[0]