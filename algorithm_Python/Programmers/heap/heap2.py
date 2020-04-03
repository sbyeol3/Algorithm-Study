import heapq as h
def solution(stock, dates, supplies, k):
    cnt = 0
    flour = stock
    date = 0
    tree = []


    for i, v in enumerate(dates) :
        h.heappush(tree, (v, supplies[i]))

    while(True) :
        arr = []
        while tree and date <= tree[0][0] and (flour-date) >= tree[0][0] :
            num = h.heappop(tree)
            d = num[0]
            s = num[1]
            h.heappush(arr,(-s,s,d))

        
        num2 = h.heappop(arr)
        flour = flour + num2[1]
        date = date + num2 [2]
        cnt = cnt+1
        if flour >= k :
            return cnt

    return cnt

stock = 4
dates = [3,4,10,15]
supplies = [3,20,5,10]
k =30

print(solution(stock,dates,supplies, k))