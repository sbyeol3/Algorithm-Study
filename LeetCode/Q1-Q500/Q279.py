class Solution:
    def numSquares(self, n: int) -> int:
        square = [i**2 for i in range(1, math.floor(n**0.5)+1)]
        dp = [0] * (n+1)
        dp[1] = 1
    
        for num in square :
            dp[num] = 1
        for i in range(2, n+1) :
            if dp[i] == 0 :
                squares = [num for num in square if num < i]
                possible = [dp[i-idx] for idx in squares]
                dp[i] = min(possible) + 1
        return dp[n]