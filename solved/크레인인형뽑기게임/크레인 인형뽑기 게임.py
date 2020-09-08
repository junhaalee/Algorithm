def solution(board, moves):

    temp = []
    size = len(board)
    for i in range(size):
        line = []
        for k in range(size-1,-1,-1):
            if board[k][i]:
                line.append(board[k][i])
        temp.append(line)

    ind = 0
    answer = []
    count = 0
    while(ind<len(moves)):
        try:
            ch = temp[moves[ind]-1].pop()
            answer.append(ch)
            if answer[-1] == answer[-2]:
                answer = answer[:-2]
                count += 2
        except:
            pass
        ind += 1

    return count