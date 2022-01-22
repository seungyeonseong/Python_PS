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

li = list(map(int,input().split()))
result =0
for i in li:
    result += i**2
print(result%10)

# +
height=[]

for _ in range(9):
    height.append(int(input()))
total = sum(height)
#print(height)
for i in range(0,9):
    for j in range(i+1,9):
        if total-(height[i]+height[j]) == 100:
            height.remove(height[i])
            height.remove(height[j])
            break
#print(height)            
height.sort()
for i in height:
    print(i)


# +
height=[]

for _ in range(9):
    height.append(int(input()))
total = sum(height)
#print(height)
for i in height:
    for j in height:
        if total-(i+j) == 100 and i != j:
            height.remove(i)
            height.remove(j)
            break
    if sum(height) == 100:
        break
#print(height)            
height.sort()
for i in height:
    print(i)
# -

print(total)


