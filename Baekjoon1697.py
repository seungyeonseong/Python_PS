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
##내풀이
#처음에 메모리초과남 -> 중복값 처리
#고치니까 시간초과남 -> 리스트에 처리 후 in 함수로 확인하니 시간이 오래걸림
##--> 리스트 값을 True/False로 처리됐는지 확인+ 값 범위제한

# +
from collections import deque 
n,k = map(int,input().split())


q = deque()
li=[False]*(100002)
q.append((n,0))
li[n] = True
while q:
    x,total = q.popleft()
    if x == k:
        break
    if li[x-1] is False and x-1 >=0:
        q.append((x-1,total+1))
        li[x-1] = True
    if li[x+1] is False and x+1 <= 100000:
        q.append((x+1,total+1))
        li[x+1] = True
    if x*2<=100000:
        if li[x*2] is False:
            q.append((2*x,total+1))
            li[2*x] = True
    
print(total)
    
    

