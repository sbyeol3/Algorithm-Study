def solution(nums):
    pick = len(nums)/2
    numsToSet = list(set(nums))
    if (len(numsToSet) <= pick) : return len(numsToSet)
    else : return pick

print(solution([3,3,3,2,2,2])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,1,2,3])) # 2