N = int(input())
profit = []
dp = [0] * (N+1)

for _ in range(N) :
    a, b = map(int, input().split())
    profit.append([a,b])

for i in range(N) :
    day, money = profit[i]
    dp[i+1] = max(dp[i], dp[i+1])
    if i + day <= N :
        dp[i+day] = max(dp[i+day], dp[i] + money)

print(dp[-1])