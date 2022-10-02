import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited, graph):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == "0" and visited[nx][ny] is False:
                visited[nx][ny] = True
                q.append((nx, ny))


m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
visited = [[False] * n for _ in range(m)]

for i in range(n):
    if graph[0][i] == "0":
        bfs(0, i, visited, graph)

answer = "NO"
for i in range(n):
    if visited[m - 1][i] is True:
        answer = "YES"
        break
print(answer)
