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
lost = [2,4]
n = 5
reserve = [1,3,5]
def solution(n, lost, reserve):
    lost2=[]
    reserve2=[]
    for i in range(1,n+1):
        if i in reserve and i in lost:
            continue
        if i in lost:
            lost2.append(i)
        if i in reserve:
            reserve2.append(i)

    answer = n-len(lost2)
    
    for i in lost2:
        if i-1 in reserve2:
            reserve2.remove(i-1)
            answer +=1
        elif i+1 in reserve2:
            reserve2.remove(i+1)
            answer +=1
    print(lost2)    
    return answer

print(solution(n,lost,reserve))


# +
#고수의 풀이
# -

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
