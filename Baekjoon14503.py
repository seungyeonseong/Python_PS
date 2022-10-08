import sys
input = sys.stdin.readline

dx= [-1,0,1,0]
dy= [0,1,0,-1]


n,m = map(int,input().split())
x,y,direct = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


visited=[[False]*m for _ in range(n)]
visited[x][y] = True
count = 1
turn_time = 0

def turn_left():
    global direct
    direct -=1
    if direct == -1:
        direct = 3

while True:
    turn_left()  #2. 현재 위치에서 왼쪽 방향으로 차례대로 탐색
    nx = x + dx[direct]
    ny = y + dy[direct]
    if 0 <= nx < n and 0 <= ny<m and visited[nx][ny] is False and graph[nx][ny]==0:
        visited[nx][ny] = True #2-1. 현재위치를 청소
        x,y = nx,ny
        count += 1
        turn_time = 0
    else: #청소할 곳 없으면 회전
        turn_time += 1

    if turn_time == 4: #네 방향 모두 돌았다면
        nx = x - dx[direct]
        ny = y - dy[direct]
        if graph[nx][ny] == 0: #벽이아니면 후진
            x,y = nx, ny
        else:             #벽이면 작동을 멈춘다
            break
        turn_time = 0

print(count)


