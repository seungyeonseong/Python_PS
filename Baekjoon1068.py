# n = 5
# parent= [-1,0,0,1,1]
# rm = 1
import sys
input = sys.stdin.readline
n = int(input())
parent = list(map(int,input().split()))
rm = int(input())

def dfs(rm,li):
    li[rm] = -2
    for idx,i in enumerate(li):
        if i ==rm:
            dfs(idx,li)

dfs(rm,parent)
cnt = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        cnt += 1
print(cnt)
print(parent)