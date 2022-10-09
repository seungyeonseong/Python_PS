import sys
input = sys.stdin.readline

x,y,w,s = map(int,input().split())

#평행으로만 이동
a = (x+y)*w
#대각선으로만 이동
if (x+y)%2==0:
    b = max(x,y)*s
else: #대각선+평행 1번
    b = (max(x,y)-1)*s+w
#평행+대각선
c = min(x,y)*s +abs(x-y)*w

print(min(a,b,c))



#메모리초과 풀이
# dp=[[0]*(y+1) for _ in range(x+1)]
#
# for i in range(1, x + 1):
#     dp[i][0] = w * i
#
# for j in range(1, y + 1):
#     dp[0][j] = w * j
# if w > s:
#     for i in range(2, x + 1, 2):
#         dp[i][0] = s * i
#     for j in range(2, y + 1, 2):
#         dp[0][j] = s * j
#
# for i in range(1, x + 1):
#     for j in range(1, y + 1):
#         dp[i][j] = min(dp[i-1][j] + w, dp[i][j - 1] + w, dp[i - 1][j - 1] + s)
#
# print(dp[x][y])
