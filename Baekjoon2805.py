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
#나무의 길이가 기준치를 초과하면 break문을 통해 끝까지 탐색하는 코드 추가해서 시간초과 해결

# +
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

result =0
start,end = 0,  max(tree)
while start <= end:
    mid = (start+end)//2
    res = 0
    for i in tree:
        if i>mid:
            res += i-mid
            if res>m:
                break
    if res >=m:
        start =mid+1
    else:
        end = mid -1

print(end)
