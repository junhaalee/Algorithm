import sys
input  = sys.stdin.readline

word, key = input().strip(),input().strip()

while(True):
    if len(word) == 0:
        print('FRULA')
        break
    
    if key in word:
        ind = word.index(key)
        word = word[:ind]+word[ind+len(key):]    
    else:
        print(word)
        break

