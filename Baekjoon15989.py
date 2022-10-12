import sys

input = sys.stdin.readline

dp = [1] * (10001)

for i in range(3,10001):
    dp[i] += dp[i - 3]
for i in range(2,10001):
        dp[i] += dp[i - 2]
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])

#n입력받아서 dp새로만드는것보다 10000개 리스트 만들어놓고 출력하는게 빠르다!