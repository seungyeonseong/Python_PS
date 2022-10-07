import sys
input=  sys.stdin.readline

n = int(input())
li = []
ans = 0
for _ in range(n):
    li.append(list(map(int,input().split())))
li = sorted(li,key = lambda x:x[0])
for i in range(n):
    ans += li[i][0]*(i+1)+li[i][1]

print(ans)