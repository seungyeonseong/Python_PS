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
n = int(input())
dis  = list(map(int,input().split()))
cost = list(map(int,input().split()))


# -

ans = 0
minVal = cost[0]
for i in range(n-1):
    if minVal > cost[i]:
        minVal = cost[i]
    ans += minVal*dis[i]
print(ans)    

visited

# +
start = 0
end =0 
ans = 0
while 1:
    if start == n:
        break
        
    for x in range(n):
        if cost[start] > cost[x]:
            end = x
            break
        
    
    d = 0
    for i in range(start,end):
        d += dis[i]
    ans += d*cost[start]
    start = end

print(ans)
# -


