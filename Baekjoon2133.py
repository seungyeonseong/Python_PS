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
#구글링

# +
n = int(input())

d =[0]*(n+1)
if n>=2:
    d[2] =3

if n>=4:
    for i in range(4,n+1):
        if i%2==0:
            d[i] = d[i-2]*3
            for j in range(4,i+1,2):
                d[i] += 2*d[i-j]
            d[i] += 2
            
print(d[n])
        
        



# +
#틀린 풀이
##접근법: 4개짜리랑 2개짜리로만 점화식 만듬,,
#틀린이유->예를 들어 6개면 4,2개짜리 말고도 6개짜리의 독자적인 타일모양이 생김

# +
import sys
input = sys.stdin.readline

n = int(input())

d =[0]*(n+1)
if n>=2:
    d[2] =3
if n >=4:
    d[4]=11
if n>=6:
    for i in range(6,n+1):
        if i%2==0:
            d[i] = 3*d[i-2]+ d[i-4]*2
            
print(d[n])
