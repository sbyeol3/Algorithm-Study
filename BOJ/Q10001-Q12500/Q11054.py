n = int(input())
nums = list(map(int, input().split()))
dp = [[1,1] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] :
            dp[i][0] = max(dp[i][0], dp[j][0]+1)
        elif nums[i] < nums[j] :
            dp[i][1] = max(dp[i][1], dp[j][0]+1, dp[j][1]+1)

result = 1
for i in range(n):
    v1, v2 = dp[i]
    result = max(result, v1, v2)
    
print(result)
