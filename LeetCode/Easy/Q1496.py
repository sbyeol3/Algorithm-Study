# 1496. Path Crossing
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        now = [0, 0]
        visit = [now]
        for p in path :
            if p == 'N' :
                now = [now[0],now[1]+1]
                if now in visit : return True
                else : visit.append(now)
            elif p == 'E' :
                now = [now[0]+1,now[1]]
                if now in visit : return True
                else : visit.append(now)
            elif p == 'S' :
                now = [now[0],now[1]-1]
                if now in visit : return True
                else : visit.append(now)
            elif p == 'W' :
                now = [now[0]-1,now[1]]
                if now in visit : return True
                else : visit.append(now)
        return False