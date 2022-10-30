import sys
input = sys.stdin.readline

n =int(input())

total = 0
li = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if li[i][j] == 1:
                continue
            else:
                li[i][j] = 1
                total +=1
print(total)
print(li)


