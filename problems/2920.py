nums = list(map(int, input().split()))

if [8,7,6,5,4,3,2,1] == nums:
    print('descending')
elif [1,2,3,4,5,6,7,8] == nums:
    print('ascending')
else:
    print('mixed')
