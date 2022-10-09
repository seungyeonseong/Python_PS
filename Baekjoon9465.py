import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dp= []
    n = int(input())
    for _ in range(2):
        dp.append(list(map(int,input().split())))

    for i in range(1,n):
        if i ==1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else:
            dp[0][i] += max(dp[1][i-1],dp[1][i-2])
            dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))


#틀린 우선순위힙 풀이ㅠ
# import heapq
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# t= int(input())
# for _ in range(t):
#     n = int(input())
#     graph=[]
#     for _ in range(2):
#         graph.append(list(map(int,input().split())))
#     total = 0
#     q = []
#     visited = [[False]*len(graph[0]) for _ in range(2)]
#
#     for i in range(2):
#         for j in range(len(graph[0])):
#             heapq.heappush(q,(-1*graph[i][j],i,j))
#     while q:
#         x,i,j = heapq.heappop(q)
#         if visited[i][j] is False:
#             total += -1*x
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0<=nx<2 and 0<= ny <len(graph[0]):
#                     visited[nx][ny] = True
#     print(total)



