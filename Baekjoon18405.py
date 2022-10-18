n,k = 3,3
graph = [[1,0,2],
         [0,0,0],
         [3,0,0]]
s,X,Y = 1,2,2

import heapq

dx = [1,0,-1,0]
dy = [0,1,0,-1]

sec = 0
q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            heapq.heappush(q,(sec,graph[i][j],i,j))
while q:
    if sec ==s:
        break
    sec,num,x,y = heapq.heappop(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <n and 0<=ny <n and graph[nx][ny]==0:
            graph[nx][ny] = num
            if sec+1!=s:
                heapq.heappush(q,(sec+1,num,nx,ny))

print(graph)
print(graph[X-1][Y-1])


##시간초과 풀이_s번 반복하면서 q만들기
#
# for _ in range(s):
#     q = []
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] > 0:
#                 heapq.heappush(q,(graph[i][j],i,j))
#     while q:
#         num,x,y = heapq.heappop(q)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx <n and 0<=ny <n and graph[nx][ny]==0:
#                 graph[nx][ny] = num
#
# print(graph[X-1][Y-1])