temp = n = int(input())
check = 0

while(True):
    ten = temp//10
    one = temp%10
    res = ten + one
    check += 1
    temp = int(str(temp%10)+str(res%10))

    if(n == temp):
        break
    
print(check)