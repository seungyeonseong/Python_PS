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

x,y,w,h = map(int,input().split())
li=[]
li.append(x)
li.append(y)
li.append(h-y)
li.append(w-x)
print(min(li))

# +
xli=[]
yli=[]
for _ in range(3):
    x,y  = map(int,input().split())
    xli.append(x)
    yli.append(y)
for i in xli:
    if xli.count(i) == 1:
        new_x = i
for j in yli:
    if yli.count(j) == 1:
        new_y = j
print(new_x, new_y)
    
    
# -

li=[1,2,3,3,3]
li.count()


