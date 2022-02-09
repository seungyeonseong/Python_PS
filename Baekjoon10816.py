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
#내풀이_정답처리이긴 한데 메모리+시간 과다..?

# +
n= int(input())
card =list(map(int,input().split()))

m = int(input())
li = list(map(int,input().split()))

def func(x,card,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if card[mid] ==x:
        return card[mid]
    elif card[mid] >x:
        return func(x,card,start,mid-1)
    else:
        return func(x,card,mid+1,end)
    
card.sort()
count={}
for i in card:
    try:count[i] += 1
    except: count[i] = 1

for x in li:
    if func(x,card,0,n-1) != None:
        print(count[x],end =" ")
    else:
        print(0,end=" ")


# +
count={}
for i in card:
    try:count[i] += 1
    except: count[i] = 1



# +
###구글링__딕셔너리 -> Counter함수 이용__시간단축,메모리증가
# -

from collections import Counter
array = Counter(card)
print(array)
