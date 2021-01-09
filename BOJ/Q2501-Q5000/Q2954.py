diary = input()
if len(diary) == 0 : print('')
p = 0
vowel = 'aeiou'
original = ''

while p <= len(diary)-1 :
    ch = diary[p]
    if ch in vowel :
        p += 3
    else : p += 1
    original += ch

print(original)