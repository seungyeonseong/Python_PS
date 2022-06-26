# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
###구글링
#dp응용 생각을 못함 ㅠ

# +
### import sys
#input = sys.stdin.readline
n,m = map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1]+ dp[i-1][j]-dp[i-1][j-1]+li[i-1][j-1]

    
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    ans = dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]
    print(ans)

# +
#내풀이 =>시간초과
# -

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dp=[]
for _ in range(n):
    li=[0]
    x = list(map(int,input().split()))
    total = 0
    for i in x:
        total += i
        li.append(total)
    dp.append(li)
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    ans = 0
    for i in range(x1-1,x2):
        ans += dp[i][y2]-dp[i][y1-1]
    print(ans)
