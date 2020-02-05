words = list(input())

result = 0

for word in words:
    if ord(word) <= ord('O'):
        result += int((ord(word)+1)/3)-19
    elif ord(word) <= ord('S'):
        result += 8
    elif ord(word) <= ord('V'):
        result += 9
    else:
        result += 10

print(result)