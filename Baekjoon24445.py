import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = True
    total[start] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)
                cnt += 1
                total[i] = cnt

n,m,r = map(int,input().split())
cnt = 1
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
total = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,n+1):
    graph[i] = sorted(graph[i],reverse=True)

bfs(r)
for i in range(1,n+1):
    print(total[i])

