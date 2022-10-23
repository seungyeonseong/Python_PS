import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q= []
    distance[start]= 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n = int(input())
m = int(input())
distance = [int(1e9)]*(n+1)
graph = [[] for _ in range(n+1)]
res = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append([b,1])
    graph[b].append([a,1])
dijkstra(1)
for i in range(2,n+1):
    if distance[i] <= 2:
        res += 1
print(res)

##플로이드 워셜-시간초과
# n = int(input())
# m = int(input())
# graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a,b= map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
# for i in range(1,n+1):
#     graph[i][i] = 0
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
#
# res = 0
# for i in range(2,n+1):
#     if graph[1][i] <=2:
#         res +=1
# print(res)