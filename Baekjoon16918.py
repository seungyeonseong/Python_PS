from collections import deque
import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())
graph=[]
for _ in range(r):
    graph.append(list(input().rstrip()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()

def bfs(q, graph): #폭탄 폭발
    while q:
        x,y = q.popleft()
        graph[x][y] = "."
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx< r and 0 <= ny <c and graph[nx][ny]=="O":
                graph[nx][ny] = "."

def simulate(sec):
    global q, graph
    if sec == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] =="O":
                    q.append((i,j))
    elif sec%2 ==1: #3초가 지난 폭탄은 폭발시킴
        bfs(q,graph)
        for i in range(r):
            for j in range(c):
                if graph[i][j] =="O":
                    q.append((i,j))
    else: #폭탄이 설치되어 있지 않은 칸에 폭탄 설치
        graph = [['O']*c for _ in range(r)]
for i in range(1,n+1):
    simulate(i)
for i in graph:
    print("".join(i))



# for i in range(r):
#     for j in range(c):
#         if graph[i][j]=="OO":
#             cnt[i][j] = 1
#         else:
#             cnt[i][j] = 0
# sec = 1
# while n >= sec:
#     q = deque()
#     while q:
#         x,y = q.popleft()
#         cnt[x][y] = 0
#     if n == sec:
#         break
#     for i in range(r):
#         for j in range(c):
#             if cnt[i][j] == 3:
#                 cnt[i][j] = 0
#                 for k in range(4):
#                     nx = i +dx[k]
#                     ny = j +dy[k]
#                     if 0<= nx <r and 0 <= ny <c:
#                         q.append((nx,ny))
#             else:
#                 cnt[i][j] += 1
#     sec +=1
# print(cnt)

# for i in range(r):
#     for j in range(c):
#         if cnt[i][j]==0:
#             print(".",end ="")
#         else:
#             print("O",end="")
#     print()