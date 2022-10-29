import sys
input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    li = list(input().rstrip())
    tmp =[]
    for idx,i in enumerate(li):
        if i == "Y":
            tmp.append(1)
        else:
            tmp.append(int(1e9))
    graph.append(tmp)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
cnt = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if i== j:
            continue
        if graph[i][j] <= 2:
            tmp += 1
    cnt = max(cnt,tmp)
print(cnt)
for i in graph:
    print(*i)

