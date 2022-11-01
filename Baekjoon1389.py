import sys
input = sys.stdin.readline
INF = int(1e9)

n,m  = map(int,input().split())



graph = [[INF]*(n+1) for _ in range(n+1)]
for  _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1,n+1):
    graph[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])
tmp = sum(graph[1])
idx = 1
for i in range(2,n+1):
    if sum(graph[i]) < tmp:
        tmp = sum(graph[i])
        idx = i

print(idx)
