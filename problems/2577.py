num1 = int(input())
num2 = int(input())
num3 = int(input())

val = list(str(num1*num2*num3))

count = {}

for nums in val:
    if nums in count.keys():
        count[nums] += 1
    else:
        count[nums] = 1

for i in range(0,10):
    try:
        print(count[str(i)])
    except:
        print(0)