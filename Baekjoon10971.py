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
#####답은 출력되지만 Python3로 제출하면 시간초과 뜬다.
##### --> PyPy3로 제출해서 맞음

# +
import sys
from itertools import permutations
#입력
input= sys.stdin.readline
n = int(input())
total = 987654321
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))
#cost =  list(list(map(int,input().split())) for _ in range(n))

city = [i for i in range(0,n)]


#경로 비용 합 구하는 함수
def sum_routes(r):
    global cost,n,total
    ans = 0
    for j in range(n-1):
        start = r[j]
        end = r[j+1]
        if  cost[start][end] == 0:
            return False
        elif cost[start][end] >= total:
            return False
        else:
            ans += cost[start][end]
    if cost[end][r[0]] < total and cost[end][r[0]] != 0:
        ans += cost[end][r[0]] 
    else:
        return False
    return ans
        
#경로 경우의 수                
per = list(permutations(city,n))        
for i in range(len(per)):
    if sum_routes(per[i]) != False:
        total = min(sum_routes(per[i]),total)
        
print(total)
# -


