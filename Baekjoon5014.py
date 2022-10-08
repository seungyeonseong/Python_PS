from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())
q = deque()
visited=[0]*(f+1)
q.append(s)
visited[s] = 1
while q:
    x = q.popleft()
    if x == g:
        break
    for i in (x+u,x-d):
        if 0<i<=f and visited[i] ==0:
            visited[i] = visited[x] + 1
            q.append(i)

if visited[g]==0:
    print("use the stairs")
else:
    print(visited[g]-1)