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
card = list(map(int,input().split()))
m = int(input())
li = list(map(int,input().split()))

def func(x,card,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if card[mid] == x:
        return mid
    elif card[mid] > x:
        return func(x,card,start,mid-1)
    else:
        return func(x,card,mid+1,end)
    
card.sort()
for x in li:
    if func(x,card,0,n-1) == None:
        print(0)
    else:
        print(1)
        
# -


