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
import heapq

def solution(jobs):
    end = 0
    start = -1
    total=[]
    q = []
    while True:
        if len(total)==len(jobs):
            return int(sum(total)/len(total)) #int안해서 오답파티함

        for i in jobs:#시작시간이 같은것
            if start < i[0] <= end:
                heapq.heappush(q,(i[1],i[0]))

        if len(q)>0:
            y,x = heapq.heappop(q)
            start = end
            end = start+y
            total.append(start-x+y)
        else:
            end += 1    ###이거를 생각못해서 삽질,,,,,
