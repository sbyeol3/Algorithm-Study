rest = 1000 - int(input())
coins= [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins :
    if rest == 0 : break
    q, r = divmod(rest, coin)
    cnt += q
    rest = r

print(cnt)