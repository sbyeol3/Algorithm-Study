def solution(skill, skill_trees):
    count = 0
    while skill_trees :
        tree = skill_trees.pop()
        idx = []
        finish = False
        impossible = False
        for s in skill :
            i = tree.find(s)
            if i != -1 and finish : 
                impossible = True
                break
            elif i == -1 : finish = True
            else : idx.append(i)
        if impossible : continue
        if (sorted(idx) == idx) : count += 1
    return count
print(solution('CBD',["BACDE", "CBADF", "AECB", "BDA"]))