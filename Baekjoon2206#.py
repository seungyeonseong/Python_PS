# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#못풀음ㅜ
#접근법: 1이 존재하는 곳 모두 한번씩 0으로 바꿔서 bfs수행해서 최솟값 얻으려고함

#--> 한번 bfs수행하면 graph값이 변하는 문제

# +
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    graph[x][y] = 1
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1 
                q.append((nx,ny))
            if graph[nx][ny] == 1:
                continue
        return graph[n-1][m-1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,list(input()))))

total =[]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] == 0
            if bfs(0,0) != 0:
                total.append(bfs(0,0))
        graph[i][j] == 1
            
print(total)
    
    

# +
###구글링

#풀이법:3차원 리스트 구현-->벽 부셨는지 여부 + 방문체크 2차원

# +
from collections import deque

n,m = map(int,input().split())
graph = []

#3차원 행렬을 통해 벽의 파괴를 파악
#visited[x][y][0]는 벽 파괴 가능/visited[x][y][1]은 불가능
visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
visited[0][0][0] = 1

for _ in range(n):
    graph.append(list(map(int,list(input()))))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    
    while q:
        a,b,c = q.popleft()
        #끝 점에 도달하면 이동 횟수를 출력
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            #다음 이동할 곳이 벽이고, 벽을 부시지 않은 경우
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                q.append((nx,ny,1))
            #다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳이면
            elif graph[nx][ny] ==0 and visited[nx][ny][c] ==0:
                visited[nx][ny][c] = visited[a][b][c] +1
                q.append((nx,ny,c))
    return -1
print(bfs(0,0,0))

# +
from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))
# -


