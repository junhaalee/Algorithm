x,y,w,h = map(int, input().split())

if x < w/2:
    width = x
else:
    width = w-x

if y < h/2:
    height = y
else:
    height = h-y

if width < height :
    print(width)
else:
    print(height)

# 숏코딩
print(min[x,y,w-x,h-y])