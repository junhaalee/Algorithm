num1 = int(input())
num2 = input()

#::의 의미
temp_num2 = num2[::-1]

for i in range(len(temp_num2)):
    print(num1*int(temp_num2[i]))
print(num1*int(num2))

