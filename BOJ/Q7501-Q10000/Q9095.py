N = int(input())
cases = []

for _ in range(N):
    case = int(input())
    cases.append(case)

maxCase = max(cases)
dp = [1,2,4] + [0] * (maxCase)

for i in range(3, maxCase):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(N):
    print(dp[cases[i]-1])