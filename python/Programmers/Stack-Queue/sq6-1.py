def solution(prices):
    length = len(prices)
    answer = [0] * length
    for i in range(length) : answer[i] = length - 1 - i 
    
    while(prices):
      tmp = prices.pop()
      for i in range(len(prices)) :
        if prices[i] > tmp :
          answer[i] = len(prices) - i

    return answer


'''
채점 결과
정확성: 66.7
효율성: 0.0
합계: 66.7 / 100.0
'''