w, h = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(h)]

w = 6
h = 4

tomato = [[0, 0, -1, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1]]


def detect(tomato):
    temp = []
    for i in range(h):
        temp += list(set(tomato[i]))
    temp = list(set(temp))
    temp.sort()
    return [temp[-1],len(temp)]

def extension(tomato):
    try:
        if tomato[i+1][j] == 0:
            tomato[i+1][j] = 1
    except:
        pass
    try:
        if tomato[i-1][j] == 0:
            tomato[i-1][j] = 1
    except:
        pass
    try:
        if tomato[i][j+1] == 0:
            tomato[i][j+1] = 1
    except:
        pass
    try:
        if tomato[i][j-1] == 0:
            tomato[i][j-1] = 1
    except:
        pass
    



count = 0
    
while(True):
    value = detect(tomato)[0]
    check = detect(tomato)[1]

    if value == 1 and check == 1:
        break
    
    elif value == 0:
        count = -1
    
    if value == 2:
        count += 1
           
     

print(count)