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
from collections import deque


n = int(input())
q=deque()
for _ in range(n):

    x = list(input().split())
    if x[0] =="push":
        q.append(x[1])
    elif x[0] =="pop":
        if len(q)>0:
            a = q.pop()
            print(a)
        else:
            print(-1)
    elif x[0] =="size":
        print(len(q))
    elif x[0]=="empty":
        if q:
            print(0)
        else:
            print(1)
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
            
        
        
    
# -

x = list(input().split())
x

# +
from collections import deque

q=deque()
q.append(3)
q.popleft()
q

# +
for tc in range(int(input())):
    k = int(input())
    li = list(map(int,input().split()))
    #li.sort()
    #40 30 30 50 -> 70 80 ->150
    
    while len(func(li)) !=1:
        total += sum(func(li))
        li = func(li)
        
    print(total)    
    
    
def func(li):
    arr=[]
    if len(li)%2 ==0:  #짝수이면
        res = 0
        for i in range(0,len(li)-1,2):
            arr.append(li[i]+li[i+1])
    else:
        for i in range(0,len(li)-2,2):
            arr.append(li[i]+li[i+1])
        arr.append(li[-1])
    return arr
            
            
    
    
# -


