def maxpath(i, j, x, y):
    path = []
    for h in range(1, x + 1):
        for v in range(1, y + 1):
            path.append([h, v, abs(i - h) + abs(j - v)])
    s = sorted(path, key=lambda tup: tup[2], reverse=True)
    return s


def yoyo (x: int, y: int, i: int, j: int):
    s = maxpath(i, j, x, y)
    print(s)
    x1, y1 = s[0][0], s[0][1]
    k=1
    maxp=0
    while (abs(s[0][0]-s[k][0])+abs(s[0][1]-s[k][1])) >= maxp and k<x*y-1:
        maxp=abs(s[0][0]-s[k][0])+abs(s[0][1]-s[k][1])
        k += 1
    x2, y2 = s[k-1][0],s[k-1][1]
    return x2, y2, x1, y1



m=input()
for c in range (int(m)):
    x,y,i,j=input().split()
    print(yoyo(int(x),int(y), int(i), int(j)))
