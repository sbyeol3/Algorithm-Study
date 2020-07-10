def solution(A,B):
    A.sort()
    B = list(reversed(sorted(B)))
    result = 0
    for i in range(len(A)) :
        result += A[i] * B[i]
    return result