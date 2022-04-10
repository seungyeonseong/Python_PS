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
answers = [1,3,2,4,2]
#answers = [1,2,3,4,5]

def solution(answers):
    answer = []
    res=[0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==a[i%len(a)]:
            res[0] += 1
        if answers[i]==b[i%len(b)]:
            res[1] += 1
        if answers[i]==c[i%len(c)]:
            res[2] += 1    
    for i in range(len(res)):
        if max(res)==res[i]:
            answer.append(i+1)
    return answer

print(solution(answers))
