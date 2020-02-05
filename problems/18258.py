import sys 

statements = sys.stdin.read().splitlines()
statements = statements[1:]

stack = []
    
def size(stack):
    print(len(stack))

def empty(stack):
    r = 0 if stack else 1
    print(r)
    
def top(stack):
    r = stack[-1] if stack else -1
    print(r)
    
for s in statements : 
    if s.find('push') != -1 : 
        stack.append(int(s[4:]))
        
    elif s == 'pop':
        r = stack.pop() if stack else -1
        print(r)
    
    else:
        eval(s+"(stack)")