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
##내풀이

# +
array = [1, 5, 2, 6, 3, 7, 4]
commands= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for x in commands:
        i,j,k = x
        li= array[i-1:j]
        li.sort()
        answer.append(li[k-1])
        
        
    return answer

print(solution(array,commands))
