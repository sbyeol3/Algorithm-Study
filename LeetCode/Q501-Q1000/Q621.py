from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 : return len(tasks)
        
        taskDict = dict(Counter(tasks))
        maxNum = 0
        maxCnt = 0
        
        for task, value in taskDict.items() :
            if value > maxNum :
                maxNum = value
                maxCnt = 1
            elif value == maxNum : maxCnt += 1
        
        if len(taskDict) <= n+1 : return (maxNum-1) * (n+1) + maxCnt
        else: return max((maxNum-1) * (n+1) + maxCnt, len(tasks))