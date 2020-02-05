n = int(input())

ans = 0

for k in range(n):
    words = list(input())
    i = 0
    check = True
    while(i < len(words)-1):
        temp = words[::-1]
        final = words[words.index(words[i]):len(words)-temp.index(words[i])]
        if len(list(set(final))) != 1:
            check = False
            break
        i += 1
    
    if check == True:
        ans += 1

print(ans)