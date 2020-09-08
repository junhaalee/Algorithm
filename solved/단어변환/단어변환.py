def dif(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count == 2:
            break
    
    if count == 2:
        return False
    else:
        return True

def solution(begin, target, words):

    if target not in words:
        return 0
    else:
        temp = [begin]

        ind = 0

        while True:

            if target in temp:
                break

            for t in temp:
                arr = []
                for i in range(len(words)):
                    if len(words[i]) == len(begin) and dif(t, words[i]):
                        arr.append(words[i])
                        words[i] = ''
            temp = arr

            ind += 1
        
        return ind