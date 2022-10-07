from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    tmp = graph[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny <n and visited[nx][ny] is False and graph[nx][ny]==tmp:
                visited[nx][ny] = True
                q.append((nx,ny))
    return

def bfs2(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    tmp = graph[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny <n and visited[nx][ny] is False and graph[nx][ny]!="B":
                visited[nx][ny] = True
                q.append((nx,ny))
    return


# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(input()))

n = 5
graph=[
['R','R','R','B','B'],
['G','G','B','B','B'],
['B','B','B','R','R'],
['B','B','R','R','R'],
['R','R','R','R','R']
]
visited=[[False]*n for _ in range(n)]
ans = [0,0]
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            bfs(i,j)
            ans[0] +=1

visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] is False and graph[i][j]=="B":
            bfs(i,j)
            ans[1] +=1
        elif visited[i][j] is False:
            bfs2(i,j)
            ans[1] +=1
print(ans[0],ans[1])