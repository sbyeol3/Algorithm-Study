class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]

        for i in range(1, n):
            dp[0] += sum([dp[j] for j in range(1, 5)])
            dp[1] += sum([dp[j] for j in range(2, 5)])
            dp[2] += sum([dp[j] for j in range(3, 5)])
            dp[3] += sum([dp[j] for j in range(4, 5)])

        return sum(dp)