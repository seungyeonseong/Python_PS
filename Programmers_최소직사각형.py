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

def solution(sizes):
    answer = [0,0]
    for x,y in sizes:
        #둘 중 길이가 더 긴 것
        answer[0] = max(answer[0],max(x,y))
        answer[1] = max(answer[1],min(x,y))

    return answer[0]*answer[1]
