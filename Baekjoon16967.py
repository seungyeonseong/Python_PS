import sys
from collections import deque
input = sys.stdin.readline

h,w,x,y = map(int,input().split())
Barray = []
for _ in range(h+x):
    Barray.append(list(map(int,input().split())))
Aarray = [ [0]*(w+y) for _ in range(h+x)]
for i in range(h):
    for j in range(w):
        Aarray[i][j] = Barray[i][j]

for i in range(x,h):
    for j in range(y,w):
        Aarray[i][j] = Barray[i][j] - Aarray[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(Aarray[i][j],end=" ")
    print()


