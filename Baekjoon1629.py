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
#시간초과->return할때마다 %c붙여서 해결

# +
a,b,c =map(int,input().split())

def recur_func(a,b):
    if b==1:
        return a
    y = recur_func(a,int(b/2))
    if b%2==0:
        return (y*y)%c
    else:
        return (y*y*a)%c
    
print(recur_func(a,b)%c)
    

