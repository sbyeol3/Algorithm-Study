N = int(input())
pc = set()
cs = list(map(int, input().split()))
total = 0
for c in cs :
    if c in pc : total += 1
    else : pc.add(c)

print(total)