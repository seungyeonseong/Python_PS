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
#아주 큰 수의 피보나치를 빠르게 구하는 방법은 행렬의 거듭제곱을 이용하는 것

#근데 이해가 잘 안되서 규칙찾아 푸는 풀이 참고했따...

# +
n = int(input())
dp =dict()
def fibo(x):
    if dp.get(x) != None:
        return dp[x]
    if x ==0:
        return 0
    elif x==1 or x==2:
        return 1
    if x%2==0:
        dp[x//2+1] = fibo(x//2+1)%1000000007
        dp[x//2-1] = fibo(x//2-1)%1000000007
        return dp[x//2+1]**2-dp[x//2-1]**2
    else:
        dp[x//2+1] = fibo(x//2+1)%1000000007
        dp[x//2] = fibo(x//2)%1000000007
        return dp[x//2+1]**2+dp[x//2]**2
    
print(fibo(n)%1000000007)

