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

card.sort()
for x in li:
    start = 0
    end = n-1
    while start <= end:
        mid  = (start+end)//2
        if x ==card[mid]:
            print(1,end=" ")
            break
        elif x > card[mid]:
            start = mid +1
        else:
            end = mid-1
        if start == end:
            print(0,end=" ")
            break
        

        
        
    

# +
n = int(input())
card = list(map(int,input().split()))
m = int(input())
li = list(map(int,input().split()))

def func(x,card,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if x ==card[mid]:
        return mid
    elif x > card[mid]:
        return func(x,card,mid +1,end)        
    else:
        return func(x,card,start,mid-1)
            
card.sort()
for x in li:
    if func(x,card,0,n-1) == None:
        print(0,end=" ")
    else:
        print(1,end=" ")

# -


