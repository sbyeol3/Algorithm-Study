N, K = map(int, input().split())
coins = []
current = K
answer = 0

for _ in range(N):
    coins.append(int(input()))

while current > 0 :
    coin = coins.pop()
    if coin > current : continue
    num, rest = divmod(current, coin)
    answer += num
    current = rest
    
print(answer)