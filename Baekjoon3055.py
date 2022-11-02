import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c = map(int,input().split())
graph= []
for _ in range(r):
    graph.append(list(input().rstrip()))

def bfs(graph):
    wq = deque()
    q = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] =="S":
                x,y = i,j
                graph[i][j] = 0
                q.append((i,j))
            elif graph[i][j] =="*":
                wq.append((i,j))
    sec = 0
    while q:
        for _ in range(len(wq)):
            a,b = wq.popleft()
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if 0 <= na <r and 0 <= nb <c and graph[na][nb] != "X" and graph[na][nb]!="D" and graph[na][nb] != sec and graph[na][nb]!="*":
                    graph[na][nb] = "*"
                    wq.append((na,nb))

        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <r and 0 <= ny <c:
                    if graph[nx][ny] == "D":
                        return graph[x][y]+1
                    elif graph[nx][ny] == ".":
                        graph[nx][ny] = graph[x][y]+1
                        sec  = graph[x][y]+1
                        q.append((nx,ny))

    return False

total = bfs(graph)
if total:
    print(total)
else:
    print("KAKTUS")
