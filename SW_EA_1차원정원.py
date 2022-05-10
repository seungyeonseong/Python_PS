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
for i in range(t):
    n,d = map(int,input().split())
    if n== 1+2*d:
        answer = 1
    elif n%(2*d+1) ==0:
        answer = n//(2*d+1)
    else:
        answer = n//(2*d+1) +1
        
    print("#%d" %(i+1),answer)
