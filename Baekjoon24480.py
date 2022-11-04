import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


n, m, r = map(int,input().split())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 1
def dfs(visited, start):
    global cnt
    visited[start] = cnt
    graph[start].sort(reverse =True)
    for i in graph[start]:
        if visited[i] ==0:
            cnt += 1
            dfs(visited,i)

dfs(visited,r)
for i in range(1,n+1):
    print(visited[i])

