from collections import deque

def solution(operations):

    deq = deque()

    for op in operations:
        
        action, num = op.split()

        if action == 'I':
            deq.append(int(num))
        elif deq:
            if num == '1':
                deq.remove(max(deq))
            else:
                deq.remove(min(deq))
    
    if deq:
        return [max(deq),min(deq)]
    else:
        return [0,0]