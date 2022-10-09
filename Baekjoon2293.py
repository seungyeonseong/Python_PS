import sys
input = sys.stdin.readline

n,k =map(int,input().split())
money=[]
for _ in range(n):
    money.append(int(input()))

#점화식

dp=[0]*(k+1)
dp[0] = 1 ###동전 하나를 사용하는 경우

for coin in money:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin] ##(i-coin)만드는 경우의 수에 + coin추가
print(dp[k])

