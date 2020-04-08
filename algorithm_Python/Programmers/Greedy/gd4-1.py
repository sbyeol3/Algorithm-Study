def solution(people, limit):
    people.sort(reverse=True)
    boat = 0
    while(people):
        person = people.pop()
        print(person)
        if person > limit / 2 :
            boat += len(people) + 1
            break

        for i in range (len(people)) :
            if (person + people[i]) <= limit :
                people.pop(i)
                break
        boat += 1
    return boat

# time exceeded 1,2,3
# print(solution([70, 80, 40,40,40],100))
# print(solution([10,20,30,40,50,60,70,80,90],100))