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
#heapq.heappush()가 알아서 정렬해주는 줄 알았는데 최소힙만 보장하는 거였음,,,

# +
import heapq

def solution(operations):
    q = [] 

    for i in operations:
        i = i.split(" ")

        if i[0] == "D" and i[1]=="1" and  q:
            q.pop()
        elif i[0] == "D" and i[1]=="-1" and  q:
            heapq.heappop(q)
        elif i[0] =="I":
            heapq.heappush(q,int(i[1]))



    if not q:
        x,y = 0,0
    else:
        x = max(q)
        y = min(q)
    answer = [x,y]

    return answer

operations = ["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]
print(solution(operations))
