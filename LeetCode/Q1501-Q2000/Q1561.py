class Solution:
    def maxCoins(self, piles) -> int:
        sortedPiles = sorted(piles, reverse=True)
        result = 0
        cnt = len(piles) / 3

        for i in range(len(piles)) :
            if not cnt : return result
            if i % 2 == 1 : 
                result += sortedPiles[i]
                cnt -= 1