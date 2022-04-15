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
#문제이해하기가 넘 더러웠다...
# -

def solution(prices):
    answer = []
    for n,i in enumerate(prices):
        t = 0
        for j in range(n,len(prices)-1):
            tmp = i
            if i <= prices[j]:
                t +=1
            else:
                break
        answer.append(t)



    return answer
