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
INF = int(1e9)


n,m = map(int,input().split())
city =[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    city[a].append((b,c))
time=[INF]*(n+1)

 
    
