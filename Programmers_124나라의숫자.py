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
###구글링
#시간초과 나는 이상한나라ㅠ
#삼진법

# +
def solution(n):
    li=['1','2','4']
    answer=""
    while n >0:
        n-=1
        answer = li[n%3]+answer
        n//=3

    return answer

print(solution(13))
