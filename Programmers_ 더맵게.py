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
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    q=[]
    answer = 0
    for i in scoville:
        heapq.heappush(q,i)
    while q:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        if first>=K and second >=K:
            return answer
        else:
            answer +=1
            heapq.heappush(q,first + second*2)
        if len(q)==1 and q[0]>=K:
            return answer
        elif len(q)==1:
            return(-1)
        
    

print(solution(scoville,K))
