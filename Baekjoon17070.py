#가로,세로,대각선으로 올 수 있는 경우의 수

import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
      li.append(list(map(int, input().split())))
dp =[[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

#첫 행에서 가로로 갈 수 있는 경우
for i in range(2,n):
      if li[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
      for j in range(2,n):
            #대각선 이동 가능한 경우
            if li[i][j] == 0 and li[i-1][j]==0 and li[i][j-1]==0:
                  dp[2][i][j] = sum(dp[k][i-1][j-1] for k in range(3))

            #가로/세로 이동 가능한 경우
            if li[i][j] == 0:
                  dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
                  dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(sum(dp[k][-1][-1]for k in range(3)))


#BFS=>시간초과
# from collections import deque
#
# # dx = [0,1,1]
# # dy = [1,0,1]
# d = [[0,1],[1,0],[1,1]]
# v = [[1,0],[1,1]]
# h = [[0,1],[1,1]]
# def check(x,y,nx,ny):
#       if nx-x==1 and ny-y==1:
#             return "d"
#       if nx==x and ny-y==1:
#             return "h"
#       else:
#             return "v"
# n = 6
# li = [[0,0,0,0,0,0],
#       [0,1,0,0,0,0],
#       [0,0,0,0,0,0],
#       [0,0,0,0,0,0],
#       [0,0,0,0,0,0],
#       [0,0,0,0,0,0]]
# res = 0
# visited = [[False]*(n) for _ in range(n)]
#
# q = deque()
# q.append(("h",0,1))
# visited[0][0] = True
# visited[0][1] = True
# while q:
#       direct,x,y = q.popleft()
#       if x==n-1 and y ==n-1:
#             res += 1
#       if direct == "d":
#             for i in range(3):
#                   nx = x + d[i][0]
#                   ny = y + d[i][1]
#                   if 0 <= nx < n and 0 <= ny < n and li[nx][ny] ==0:
#                         direct = check(x,y,nx,ny)
#                         if direct =="d":
#                               if li[nx-1][ny] != 0 or li[nx][ny-1]!=0:
#                                     continue
#                         q.append((direct,nx,ny))
#                         visited[nx][ny] = True
#                         # if nx == n - 1 and ny == n - 1:
#                         #       res += 1
#       elif direct == "v":
#             for i in range(2):
#                   nx = x + v[i][0]
#                   ny = y + v[i][1]
#                   print(nx,ny)
#                   if 0 <= nx < n and 0 <= ny < n and li[nx][ny] ==0:
#                         direct = check(x,y,nx,ny)
#                         if direct =="d":
#                               if li[nx-1][ny] != 0 or li[nx][ny-1]!=0:
#                                     continue
#                         q.append((direct,nx,ny))
#                         visited[nx][ny] = True
#                         # if nx == n - 1 and ny == n - 1:
#                         #       res += 1
#       elif direct == "h":
#             for i in range(2):
#                   nx = x + h[i][0]
#                   ny = y + h[i][1]
#                   if 0 <= nx < n and 0 <= ny < n and li[nx][ny] ==0:
#                         direct = check(x,y,nx,ny)
#                         if direct =="d":
#                               if li[nx-1][ny] != 0 or li[nx][ny-1]!=0:
#                                     continue
#                         q.append((direct,nx,ny))
#                         visited[nx][ny] = True
#                         # if nx == n - 1 and ny == n - 1:
#                         #       res += 1
# print(*visited)
# print(res)