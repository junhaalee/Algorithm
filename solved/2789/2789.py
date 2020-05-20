temp = list('CAMBRIDGE')

word = list(input().strip())

for t in temp:

    while(True):
        if t not in word:
            break
        else:
            word.remove(t)

print(''.join(word))