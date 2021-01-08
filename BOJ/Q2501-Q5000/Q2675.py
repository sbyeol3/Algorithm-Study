N = int(input())
s = []

for _ in range(N) :
    a, b = input().split()
    string = ''
    for i in range(len(b)):
        string += b[i] * int(a)
    s.append(string)

for i in range(N) :
    print(s[i])