# import sys
# input  = sys.stdin.readline

# word, key = input().strip(),input().strip()

# word, key = 'mirkovC4nizCC44', 'C4'

# while(True):

#     if key not in word:
#         if len(word) == 0:
#             print('FRULA')
#             break
#         else:
#             print(word)
#             break

#     else:   
#         ind = []
#         for i in range(len(word)-len(key)+1):
#             if key == word[i:i+len(key)]:
#                 ind.append(i)

#         while(ind):
#             i = ind.pop()
#             word = word[:i]+word[i+len(key):]
