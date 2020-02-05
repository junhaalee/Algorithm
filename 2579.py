# # 방법 1 - 메모리 초과
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# temp = [[nums[::-1],0,0]]

# while(True):
    
#     stop = n+1
    
#     for i in range(len(temp)):
#         if stop > temp[i][2]: stop = temp[i][2]
#     if stop >= n-2:
#         break

#     arr_temp = []
    
#     for i in range(len(temp)): 
#         arr=[]
#         if temp[i][1] == 1:
#             if temp[i][2]+2 <= len(temp[i][0])-1:
#                 arr = temp[i][0][:]
#                 arr[temp[i][2]+2] += arr[temp[i][2]]
#                 arr_temp.append([arr, 2, temp[i][2]+2])
#             else:
#                 arr_temp.append(temp[i])
#         else:
#             if temp[i][2]+1 <= len(temp[i][0])-1:
#                 arr = temp[i][0][:]
#                 arr[temp[i][2]+1] += arr[temp[i][2]]
#                 arr_temp.append([arr, 1, temp[i][2]+1])
#                 if temp[i][2] != len(temp[i][0])-2:
#                     arr=[]
#                     arr = temp[i][0][:]
#                     arr[temp[i][2]+2] += arr[temp[i][2]]
#                     arr_temp.append([arr, 2, temp[i][2]+2])
#             else:
#                 arr_temp.append(temp[i])
#     temp = arr_temp


# ans = 0
# for i in range(len(temp)):
#     if ans < max(temp[i][0]): ans = max(temp[i][0])

# print(ans)



#방법2 - 그냥 틀림
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

def sol(nums, n):

    result = []

    result.append(nums[0])
    if n == 1:
        return result[-1]

    result.append(nums[1]+result[0])
    if n == 2:
        return result[-1]  

    result.append(max(nums[0]+nums[1],nums[0]+nums[2],nums[1]+nums[2]))
    if n == 3:
        return result[-1]

    for i in range(3, n):
        result.append(max(nums[i]+result[i-2], nums[i]+nums[i-1]+result[i-3]))

    if n > 3:
        return result[-1]

print(sol(nums, n))