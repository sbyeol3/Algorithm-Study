# 859. Buddy Strings
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) : return False
        elif A == B : 
            setA = list(set(list(A)))
            if len(setA) < len(A) : return True
            else : return False
        
        diff = []
        for i in range(len(A)) :
            if A[i] != B[i] : 
                if len(diff) == 2 : return False
                else : diff.append(i)
        
        if len(diff) < 2 : return False
        listA = list(A)
        temp = listA[diff[0]]
        listA[diff[0]] = listA[diff[1]]
        listA[diff[1]] = temp
        return ''.join(listA) == B
        