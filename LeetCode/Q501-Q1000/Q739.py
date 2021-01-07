class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
            
        for i in range(len(T)) :
            for j in range(i+1, len(T)) :
                if T[i] < T[j] :
                    result[i] = j-i
                    break
                    
        return result

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
            
        for i,v in enumerate(T):
            while stack and stack[-1][1] < v:
                t = stack.pop()
                result[t[0]] = i - t[0]
            stack.append((i,v))    
    
        return result