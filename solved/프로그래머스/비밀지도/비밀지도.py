def solution(n, arr1, arr2):

    answer = []

    
    for i in range(n):

        temp = ''

        arr1_bin = bin(arr1[i])[2:]
        arr2_bin = bin(arr2[i])[2:]
        
        arr1[i] = arr1_bin if len(arr1_bin) == n else '0'*(n-len(arr1_bin))+arr1_bin
        arr2[i] = arr2_bin if len(arr2_bin) == n else '0'*(n-len(arr2_bin))+arr2_bin

        for k in range(n):

            if arr1[i][k] == '1' or arr2[i][k] == '1':
                temp += '#'
            else:
                temp += ' '
        
        answer.append(temp)

    return answer