words = list(input().lower())
word_count = {}

for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

result = sorted(word_count.items(), key = (lambda x : x[1]), reverse=True)

if len(result) == 1:
    print(str(result[0][0]).upper())
elif result[0][1] == result[1][1]:
    print('?')
else:
    print(str(result[0][0]).upper())