n = int(input())

temp = [n]
count = 0

while(True):

    if 1 in temp:
        print(count)
        break
    nums = []
    for num in temp:
        if num%2 == 0:
            nums.append(num/2)
        if num%3 == 0:
            nums.append(num/3)
        nums.append(num-1)
    temp = nums
    count += 1

