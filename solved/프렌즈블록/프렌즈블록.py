import numpy as np

def solution(m, n, board):

    board = [list(b) for b in board]

    count = 0
    while(True):

        rem = []

        for x in range(m):
            for y in range(n):
                rem = find(m,n,x,y,board,rem)
        
        if rem:
            
            stack = [list(x[::-1]) for x in list(np.transpose(board))]

            for r in rem:
                stack[r[1]].append('0')
            
            rem = sorted([[x[1],m-1-x[0]] for x in rem], key = lambda x : x[0], reverse=True)

            for r in rem:
                stack[r[0]].pop(r[1])
                count += 1
            
            board = [list(x) for x in np.transpose(stack)][::-1]

        else:
            break
        
    return count

def find(m,n,x,y,board,rem):

    result = True
    dx = [0,0,1,1]
    dy = [0,1,0,1]
    word = board[x][y]
    if word != '0':
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0<= tx < m) and (0<= ty < n) and board[tx][ty] == word:
                pass
            else:
                result = False

        if result:
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if [tx,ty] not in rem:
                    rem.append([tx,ty])
    return rem