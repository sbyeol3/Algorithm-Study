n = int(input())
score = []
for _ in range(n): score.append(int(input()))

dp = [0] * 300
dp[0] = score[0]

for i in range(1, n):
    if i == 1 : dp[1] = dp[0] + score[1]
    elif i == 2 : dp[2] = max(score[0], score[1])+score[2]
    else : dp[i] = max(dp[i-3] + score[i-1], dp[i-2]) + score[i]

print(dp[n-1])