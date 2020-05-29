import heapq
def solution(stock, dates, supplies, k):
    cnt = 0
    start = 0
    h = []
    while (stock<k) :
        for i in range(start,len(dates)):
            if dates[i] <= stock :
                heapq.heappush(h,(-supplies[i],supplies[i]))
                start = i + 1
            else :
                break
        stock+=heapq.heappop(h)[1]
        cnt+=1
    return cnt