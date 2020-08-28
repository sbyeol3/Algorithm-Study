class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        top = len(cost)
        step = [0] * top
        step[0] = cost[0]
        step[1] = cost[1]
        
        for i in range(2, top) :
            step[i] = min(step[i-2], step[i-1]) + cost[i]
        
        return min(step[top-1], step[top-2])