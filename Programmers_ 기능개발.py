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
import math
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    li=[]
    for i in range(len(progresses)):
        li.append(math.ceil((100-progresses[i])/speeds[i]))
    tmp = li[0]
    num=0
    for i in li:
        if tmp >= i:
            num +=1
        else:
            answer.append(num)
            num = 1
            tmp = i
    answer.append(num)
            
    return answer

print(solution(progresses,speeds))
