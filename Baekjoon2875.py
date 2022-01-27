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
#입력
n, m, k = map(int,input().split())

#대회 출전 가능한 팀 수
team = 0
while n > 1 and m > 0:
    n -= 2
    m -= 1
    team += 1
#print(team)

#인턴십으로 빠져야 하는 팀 수
intern = 0
num = n+m    

if num < k:
    k -= num
    if k%3 == 0:
        intern = k//3
    else:
        intern = (k//3)+1
        
print(team-intern)
# -


