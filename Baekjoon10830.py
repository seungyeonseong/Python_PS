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
##거듭제곱 풀이=> 분할정복
#그냥풀면 시간초과남 ㅠ

# +
N,B = 2,5
A =[[1,2],[3,4]]
''''
N,B = map(int,input().split())
A =[]
for _ in range(N):
    A.append(list(map(int,input().split())))
'''

def func(N,X,A):
    li=[]
    for i in range(N):
        l=[]
        for j in range(N):
            x = 0
            for k in range(N):
                x += X[i][k]*A[k][j]
            l.append(x%1000)
        li.append(l)
    return li

def divide(A,B,N):
    if B==1:
        return A
    elif B==2:
        return func(N,A,A)
    else:
        tmp = divide(A,B//2,N)
        if B%2==0:
            return func(N,tmp,tmp)
        else:
            return func(N,func(N,tmp,tmp),A)
res = divide(A,B,N)
        
for i in res:
    for j in i:
        print(j%1000,end=" ")
    print()

