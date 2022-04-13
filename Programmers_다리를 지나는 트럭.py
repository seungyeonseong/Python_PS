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
#내풀이,,큐로 풀다가 난리남
#고수의 풀이ㅡㅡ근데 시간초과 남
#[0,0]->[0,트럭]->[트럭,0] 이릏게 구현

# +
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0]*bridge_length
    
    while q:
        answer += 1
        q.pop(0)
        total = sum(q)
        if truck_weights:
            if total + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
                
    return answer

truck_weights = [7,4,5,6]
weight= 10
bridge_length = 2

print(solution(bridge_length, weight, truck_weights))

