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
a =[]

#n번 반복
for i in range(0,n):
    cnt=0    
    score=0  
    a = list(input())
    for j in range(len(a)):
        if a[j] == "O":
            cnt += 1       #연속 점수
            score += cnt   #총 점수
        else:
            cnt = 0
    print(score)
    


# +
a,b,c = map(int,input().split())

#총생산비용
price = c
if b >= c:
    print(-1)
else:
    n = a// (c-b)
    print(n+1)
# -


3+2*n <1*n 
