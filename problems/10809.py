from collections import Counter

alph = list('abcdefghijklmnopqrstuvwxyz')

words = list(input())

words = 'baekjoon'

ans = ''

for al in alph:
    try:
        ans += str(words.index(al))+' '
    except:
        ans += '-1 '

print(ans)
