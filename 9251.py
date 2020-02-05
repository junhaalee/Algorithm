from itertools import permutations

fir = list(input())
sec = list(input())

# fir = list('ACAYKP')
# sec = list('CAPCAK')

i = min([len(fir),len(sec)])


while(i >= 1):

    check = True
    
    temp_fir = list(permutations(fir,i))
    temp_sec = list(permutations(sec,i))

    for lcs in temp_fir:
        if lcs in temp_sec:
            check = False
            # break

    if check:
        i -= 1
    else:
        # break
        pass


print(i)

