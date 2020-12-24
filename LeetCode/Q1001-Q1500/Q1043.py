class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        length = len(arr)
        dp = [0] * length
        maxNum = arr[0]
        
        for i in range(k) :
            maxNum = max(maxNum, arr[i])
            dp[i] = maxNum * (i+1)

        for i in range(k,length):
            sub = arr[i]
            for size in range(1, k+1):
                sub = max(sub, arr[i-size+1])
                dp[i] = max(dp[i], dp[i-size]+sub*size)
 
        return dp[length-1]
