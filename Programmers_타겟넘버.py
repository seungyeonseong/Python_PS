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
#내풀이

# +
from itertools import product

#numbers = [1,1,1,1,1]
numbers = [4,1,2,1]
target = 4

def solution(numbers, target):
    answer = 0
    li = [1,-1]
    result = list(product(li,repeat=len(numbers)))
    for n in result:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]*n[i]
        if total ==target:
            answer +=1
    
    return answer

print(solution(numbers,target))

# +
#고수의 풀이_재귀함수를 이용한 DFS 풀이
# -

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
