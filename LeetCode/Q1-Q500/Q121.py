class Solution:
    def maxProfit(self, prices):
        profit = [0] * len(prices)
        maximumProfit = 0
        
        for i in range(1,len(prices)) :
            profit[i] = prices[i] - min(prices[:i])
            if (profit[i] > maximumProfit) : maximumProfit = profit[i]
                
        return maximumProfit