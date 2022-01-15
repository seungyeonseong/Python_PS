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

while (1):
    li = list(map(int,input().split()))
    li.sort()
    a=li[0]
    b=li[1]
    c =li[2]
    print(a,b)
    if a==0 and b==0 and c==0:
        break
    if a**2+b**2==c**2:
        print("right")
    else:
        print("wrong")


