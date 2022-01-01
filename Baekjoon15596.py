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
#a: 합을 구해야하는 정수 n개가 저장되어 있는 리스트
#리턴값: a에 포함되어 있는 정수 n개의 합

#정수 n개가 주어졌을 때, n개의 합을 구하는 함수 작성
n = int(input())

a = list(map(int,input().split()))

#제출 형식에 맞게
def solve(li):
    total = 0
    for i in li:
        val = i
        total += val
    return total

solve(a)
# -


