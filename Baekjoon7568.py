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
n,c = map(int,input().split())
home = []
for i in range(n):
    home.append(int(input()))
ans =987654321
home.sort()
wifi = []
wifi.append(home[0])
wifi.append(home[-1])
c -= 2
if c ==0:
    print(wifi[1]-wifi[0])
else:
    start = 1
    end = n-2
    while c > 0 and start <= end:
        mid = (start+end)//2
        wifi.append(home[mid])
        c -= 1
        end = mid-1
    wifi.sort()
    for x in range(len(wifi)-1):
        if wifi[x+1]-wifi[x] <= ans:
            ans = wifi[x+1]-wifi[x]
    print(ans)
        
    
    
    
# -

print(wifi)

# +
n = int(input())
height = []
weight = []
for i in range(n):
    a,b = map(int,input().split())
    weight.append(a)
    height.append(b)

for i in range(n):
    ans = 1
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            ans += 1
    print(ans)
# -

weight

height


# +

for i in range(n):
    ans = 1
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            ans += 1
    print(ans)
# -


