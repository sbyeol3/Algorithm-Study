A, B, V = map(int, input().split())
add = 1 if (V-A) % (A-B) == 0 else 2
print((V-A) // (A-B) + add)