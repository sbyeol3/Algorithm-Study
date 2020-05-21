def solution(people, limit):
    people.sort(reverse=True)
    boat = 0
    start = 0
    end = len(people)-1

    while(start!=end):
        person = people[end]
        stop = True
        
        for i in range (start, end) :
            if (person + people[i]) <= limit :
                boat += (i-start)
                start = i+1
                stop = False
                break

        if stop : 
            boat += (end-start+1)
            break

        end -= 1
        boat += 1
        if(start==end) : boat += 1

    return boat

# time exceeded 1
# 80 70 50 50 
# print(solution([70, 60, 80, 50],100))
print(solution([10,20,30,40,50,60,70,80,90], 100))
