def solution(prices):
    leng = len(prices)
    answer = [0] * leng
    for i in range(leng) :
        answer[i] = leng-1-i
    max = 0

    for i,price in enumerate(prices):
        if price > max :
            max = price
        else :
            for j in range(0,i):
                if prices[j] > price:
                    answer[j] = i-j

    return answer

      


prices = [1, 2, 3, 2, 3]
print(solution(prices))