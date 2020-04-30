def solution(people, limit):
    people.sort(reverse=True)
    boat = 0
    start = 0
    while(people):
        person = people.pop()
        if person > limit / 2 :
            boat += len(people) + 1
            break
        
        for i in range (start, len(people)) :
            if (person + people[i]) <= limit :
                people.pop(i)
                start = i
                break
        boat += 1
    return boat

# time exceeded 1