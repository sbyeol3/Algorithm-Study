N = int(input())
times = list(sorted(list(map(int, input().split()))))
total = 0

for i in range(N):
    total += (N-i) * times[i]
print(total)