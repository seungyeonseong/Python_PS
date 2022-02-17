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

t = int(input())
for _ in range(t):
    n = int(input())
    d=[[0,0] for _ in range(n+1)]
    
    d[0][0] = 1
    if n >= 1:
        d[1][1] = 1
    if n >1:
        for i in range(2,n+1):
            d[i][0] = d[i-1][0]+d[i-2][0]
            d[i][1] = d[i-1][1]+d[i-2][1]
            
    print(d[n][0],d[n][1])


# +
###아래는 시간 초과 풀이

# +

def fibo(n,li):
    if n == 0:
        li[0] += 1
        #print(0,end=" ")
        return li
    elif n == 1:
        li[1] += 1
        #print(1,end =" ")
        return li
    else:
        return fibo(n-1,li) + fibo(n-2,li)


t = int(input())
for _ in range(t):
    n = int(input())
    li=[0,0]
    if fibo(n,li) != 0:
        print(li[0],end=" ")
        print(li[1])
            
    
    
    
