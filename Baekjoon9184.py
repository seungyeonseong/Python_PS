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
#0~20까지 초기화해놓으면 연산횟수줄어서 속도가 빨라짐
# -

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20,20,20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b and b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]
dp=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    a,b,c = map(int,input().split())
    if a ==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d" %(a,b,c,w(a,b,c)))
    
