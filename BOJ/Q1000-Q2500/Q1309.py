N = int(input())
dp = [0] * (N if N > 2 else 2)
dp[0] = 3
dp[1] = 7

for i in range(2, N):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901
print(dp[N-1])