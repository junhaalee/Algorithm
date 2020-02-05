from collections import deque

def sol(temp):
    arr = []
    temp = deque(temp)

    try :
        while(temp != 0):

            if temp[0] == '[' or temp[0] == '(':
                arr.append(temp.popleft())

            else:
                try:
                    if arr[-1]+temp[0] == '()' or arr[-1]+temp[0] == '[]':
                        arr.pop()
                        temp.popleft()
                    else:
                        arr.append(temp.popleft())
                except:
                    arr.append(temp.popleft())
    except :
        if len(arr) + len(temp) != 0:
            print('no')
        
    if len(arr) == 0 : print('yes')

while(True):
    text = input()
    if text == '.':
        break
    temp = []
    for i in range(len(text)):
        if text[i] == '(' or text[i] == ')' or text[i] == '[' or text[i] == ']':
            temp.append(text[i])
    sol(temp)