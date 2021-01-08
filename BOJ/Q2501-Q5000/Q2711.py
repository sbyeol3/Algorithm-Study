N = int(input())
result = []
for _ in range(N):
    p, word = input().split()
    pos = int(p)
    result.append(word[:pos-1]+word[pos:])

for i in range(N):
    print(result[i])