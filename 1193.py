
def sol():

    N = int(input())
    
    fin = 1
    lay = 1
    
    while N > fin :
        
        fin += lay+1
        lay += 1
        
        
    diff = fin - N
    
    if lay%2 == 1:
        m = lay-diff
        s = 1+diff
        
    else:
        m = 1+diff
        s = lay-diff
    
    print(str(s)+'/'+str(m))