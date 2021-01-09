n = int(input())
shops = list(map(int, input().split()))
milk, answer = 0, 0

for shop in shops :
    if shop == milk :
        answer += 1
        milk = (milk+1) % 3

print(answer)