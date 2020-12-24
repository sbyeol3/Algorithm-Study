class Solution:
    def isBoomerang(self, points) -> bool:
        tuplePoints = list(set(map(tuple, points)))
        xPoints = list(set(list(zip(*points))[0]))
        yPoints = list(set(list(zip(*points))[1]))
        
        if len(list(tuplePoints)) != 3 or len(xPoints) == 1 or len(yPoints) == 1  : return False
        if len(xPoints) == 2 or len(yPoints) == 2  : return True
    
        slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        slope2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        return False if slope1 == slope2 else True