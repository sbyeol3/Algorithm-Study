def solution(prices): 
    answer = [0] * len(prices) 

    for i in range(len(prices)-1): 
        for k in range(i,len(prices)-1): 
            if prices[i] > prices[k]: break 
            else: answer[i] += 1 
    
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))