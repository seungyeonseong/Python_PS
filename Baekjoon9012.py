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

n = int(input())
#')'는 '('보다 항상 개수가 적어야함 
for i in range(n):
    li = list(input())
    left=0
    right=0    #하나만 있는 경우
    case=0
    for j in range(len(li)):
        if li[j] == '(' :
            left += 1
        elif li[j] == ')':
            if left <= right:
                right += 1
                case += 1
            else:
                right += 1
        
    if case == 0 and left == right:
        print("YES")
    else:
        print("NO")


