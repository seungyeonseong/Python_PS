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

a,b = map(str,input().split())
n = 1
while b!=a:
    if int(b[-1])%2==0:
        b = int(b)//2 
        b = str(b)
        n += 1
    elif b[-1]=="1":
        b = b[:-1]
        n += 1
    else:
        n =  -1
        break
    
    if int(b)<int(a):
        n =-1
        break
print(n)
       


#
