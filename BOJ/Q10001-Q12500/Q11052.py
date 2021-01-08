N = int(input())
dp = list(map(int, input().split()))

for i in range(1,N):
    for j in range(i):
        dp[i] = max(dp[i-j-1]+dp[j], dp[i])

print(dp[-1])
