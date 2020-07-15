class Solution:
    def groupThePeople(self, groupSizes):
        length = len(groupSizes)
        answer = []
        for id in range(length) :
            size = groupSizes[id]
            if size == -1 : continue
            arr = [id]
            for j in range(id+1,length) :
                if len(arr) == size : break
                if groupSizes[j] == size : 
                    arr.append(j)
                    groupSizes[j] = -1
            answer.append(arr)
        return answer