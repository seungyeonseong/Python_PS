import sys
input = sys.stdin.readline
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
INF = int(1e9)
r,c = map(int,input().split())
graph= []
for _ in range(r):
    graph.append(list(input().strip()))

#불이 다 번지는데 걸리는 시간
qf = deque()
q = deque()
fire_visited = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]


for i in range(r):
    for j in range(c):
        if graph[i][j] =="J":
            q.append((i,j))
            visited[i][j] = 1
        if graph[i][j]=="F":
            qf.append((i,j))
            fire_visited[i][j] = 1

while qf:
    x,y = qf.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <r and 0 <= ny <c and fire_visited[nx][ny] ==0 and graph[nx][ny] !="#":
            fire_visited[nx][ny] = fire_visited[x][y]+1
            qf.append((nx,ny))

print(fire_visited)

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <r and 0 <= ny <c and visited[nx][ny] ==0 and graph[nx][ny] ==".":
            #if fire_visited[nx][ny] > visited[x][y] + 1:
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))
print(visited)
ans = int(1e9)
for i in [0,r-1]:
    for j in range(c):
        if (fire_visited[i][j]==0 and visited[i][j]!=0):
            ans = min(visited[i][j],ans)
        if (visited[i][j]!=0 and visited[i][j] < fire_visited[i][j]):
            ans = min(visited[i][j],ans)
for i in range(r):
    for j in [0,c-1]:
        if (fire_visited[i][j]==0 and visited[i][j]!=0):
            ans = min(visited[i][j],ans)

        if (visited[i][j]!=0 and visited[i][j] < fire_visited[i][j]):
            ans = min(visited[i][j],ans)

if ans == int(1e9):
    print("IMPOSSIBLE")
else:
    print(ans)
