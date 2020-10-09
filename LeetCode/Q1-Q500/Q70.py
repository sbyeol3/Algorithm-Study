class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1) : return 1
        elif (n == 2) : return 2
        
        stair0 = 1
        stair1 = 2
        
        for i in range(2,n) :
            temp = stair1
            stair1 = stair0 + stair1
            stair0 = temp
        
        return stair1
