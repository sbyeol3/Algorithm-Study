class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:        
        for piece in pieces :
            if piece[0] not in arr : return False
            startIdx = arr.index(piece[0])
            for i in range(len(piece)) :
                if startIdx >= len(arr) or piece[i] != arr[startIdx] : return False
                startIdx += 1
        
        return True