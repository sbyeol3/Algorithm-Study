def solution(arr1, arr2):
    answer = []
    m, h, n = len(arr1), len(arr2), len(arr2[0])
    
    for i in range(m):
        nums = []
        for j in range(n) :
            num = 0
            for k in range(h): num += arr1[i][k] * arr2[k][j]
            nums.append(num)
        answer.append(nums)
    
    return answer