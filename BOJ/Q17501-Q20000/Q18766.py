import sys
from collections import Counter

T = int(input())

def isCheater(original, memory) :
    for card in original.keys():
        if card not in memory or original[card] != memory[card]:
            return True
        
    return False
    
for _ in range(T):
    n = int(input())
    original = dict(Counter(list(sys.stdin.readline().split())))
    memory = dict(Counter(list(sys.stdin.readline().split())))
    result = isCheater(original, memory)

    print('CHEATER' if result else 'NOT CHEATER')

