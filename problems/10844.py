n = int(input())

# Brute Force
# def sol(n):

#     ans = False

#     if len(str(n)) == 1:
#         ans = True
    
#     else:
#         temp = list(str(n))
#         check = 0
#         for i in range(len(temp)-1):
#             if abs(int(temp[i])-int(temp[i+1])) != 1:
#                 break
#             check += 1
#         if abs(int(temp[-2])-int(temp[-1])) == 1 and check == len(temp)-1:
#             ans = True
    
#     return ans

# count = 0
# for i in range(10**(n-1), 10**n):
#     if sol(i):
#         count += 1
# print(count)

nums = [i for i in range(1,10)]

if n == 1:
    print(len(nums))
else:
    for _ in range(n-1):
        temp = []
        for num in nums:
            if str(num)[-1] == '0':
                temp.append(int(str(num)+str(1)))
            elif str(num)[-1] == '9':
                temp.append(int(str(num)+str(8)))
            else:
                temp.append(int(str(num)+str(int(str(num)[-1])-1)))
                temp.append(int(str(num)+str(int(str(num)[-1])+1)))
        nums = temp
    print(len(nums))

