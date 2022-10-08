import sys
from collections import deque, defaultdict

input = sys.stdin.readline
INF = int(1e9)
def bfs(k,v):
    visited = [False]*(n+1)
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i[0]] is False and i[1] >= k:
                q.append(i[0])
                cnt += 1
                visited[i[0]] = True

    return cnt

n,Q = map(int,input().split())
graph = defaultdict(list)
for _ in range(n-1):
    p,q,r = map(int,input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

for _ in range(Q):
    k,v = map(int,input().split())
    print(bfs(k,v))






#플로이드워셜 풀이(시간초과)
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# #n,q = map(int,input().split())
# n,Q = 4,3
# graph = [[INF]*(n+1) for _ in range(n+1)]
# for _ in range(n-1):
#     p,q,r = map(int,input().split())
#     graph[p][q] = r
#     graph[q][p] = r
#
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(i+1,n+1):
#             if graph[i][j] == INF:
#                 graph[i][j] = min(graph[i][k],graph[k][j])
#
# for _ in range(Q):
#     k,v = map(int,input().split())
#     res = 0
#     for i in range(1,n+1):
#         if i==v:
#             continue
#         if graph[v][i] >= k:
#             res +=1
#     print(res)

