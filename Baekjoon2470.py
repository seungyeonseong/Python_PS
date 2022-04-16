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
##이분탐색으로 두개 용액의 합 최솟값 찾기=> 아예 생각 x

#while문에 start <= end조건으로 설정해서 틀림,,두 용액이니까
#while start < end: 여야한다

# +
#import sys
#input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
li.sort()
start = 0
end = len(li)-1
total = li[start]+li[end]
answer=[li[start],li[end]]
while start < end:
    if abs(li[start]+li[end])< abs(total):
        total = li[start]+li[end]
        answer=[li[start],li[end]]
        if total ==0:
            break
    if li[start]+li[end]<0:
        start +=1
    else:
        end -=1
for i in answer:
    print(i,end= " ")
