#다익스트라 알고리즘 적용 아이디어
#시작노드를 0, 도착노드 D
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n,d = map(int,input().split())
graph = [[] for _ in range(d+1)]
for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    start,end, length = map(int,input().split())
    if end > d:
        continue
    graph[start].append((end,length))

distance = [INF]*(d+1)
distance[0]=0
q = []
heapq.heappush(q,(0,0))
while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[d])



