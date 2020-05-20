def solution(n):
    binary = str(bin(n))[2:]
    if len(set(binary)) == 1 : return int('10' + binary[1:],2)
    one = binary.count('1')

    while(True):
        n += 1
        if str(bin(n))[2:].count('1') == one : return n
        

print(solution(78))
print(solution(15))