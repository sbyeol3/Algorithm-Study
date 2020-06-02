def solution(dirs):
    s = { 'U':10, 'L':0, 'R':1, 'D':0 }
    p = { 'U':1, 'L':-1, 'R':1, 'D':-1 }
    v_step = []
    h_step = []
    x, y = 5, 5
    for d in dirs:
        step = y * 10 + x + s[d]
        if d == 'U' or d == 'D':
            if y + p[d] > 10 or y + p[d] < 0 : continue
            y += p[d]
            if step not in v_step : v_step.append(step)
        else :
            if x + p[d] > 10 or x + p[d] < 0 : continue
            x += p[d]
            if step not in h_step : h_step.append(step)
    return len(v_step) + len(h_step)

# 1, 4, 5, 17-20 FAIL
# print(solution("ULURRDLLU"))
print(solution("UUUUDUDUDUUU"))