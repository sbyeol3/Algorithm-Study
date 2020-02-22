def solution(numbers):
    if len(numbers) == 1 :
        num = int(numbers)
        if num in [1,2,3,5,7,9] : return 1
        else : return 0
    
    nums = [0]*10
    for num in numbers:
      i = int(num)
      nums[i] = nums[i] + 1

    print(nums)
    answer = 0
    return answer

numbers = "011"
print(solution(numbers))