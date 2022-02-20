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
###구글링 -> 규칙찾기 실패,,

# +
n = int(input())
li=[0]+list(map(int,input().split()))

#20 10 30 20 30 50 --> 4개
d = [1]*(n+1)

if n>= 2:
    for i in range(2,n+1):
        for j in range(1,i):
            if li[i] > li[j]:
                d[i] = max(d[j]+1,d[i])
        
print(max(d))
    
