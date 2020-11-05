import sys
input = sys.stdin.readline

words = [input().strip() for _ in range(int(input()))]
dic = dict()

for w in words:
    i = 0
    while w:
        if w[i] in list(dic.keys()):
            dic[w[i]] += 10**(len(w)-1)
        else:
            dic[w[i]] = 10**(len(w)-1)
        w = w[1:]

nums = sorted(list(dic.values()),reverse=True)

ans, ind = 0,9
for num in nums:
    ans += num*ind
    ind -= 1
print(ans)


#왜 안되는지 모르겠음
# import sys
# input = sys.stdin.readline

# words = [input().strip() for _ in range(int(input()))]

# ans = []
# temp = words[::]
# dic = dict()
# nums = [str(n) for n in range(10)]

# while temp:

#     temp = sorted(temp, key = lambda x : len(x), reverse = True)

#     if temp[0]:
#         if temp[0][0] not in list(dic.keys()):
#             dic[temp[0][0]] = nums[-1]
#             nums = nums[:-1]
#         temp[0] = temp[0][1:]
#     else:
#         temp.remove(temp[0])

# for i in range(len(words)):
#     a = ''
#     for k in range(len(words[i])):
#         a += dic[words[i][k]]
#     ans.append(int(a))

# print(sum(ans))