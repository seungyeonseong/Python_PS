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
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = "{{20,111},{111}}"

def solution(s):
    answer = []
    li = []
    q = deque()
    for i in s:
        if i=="}" or i ==",":
            num="".join(q)
            li.append(num)
            q=deque()
        elif i=="{":
            continue
        else:
            q.append(i)

    d = dict()
    for i in li:
        if i=="":
            continue
        if i in d:
            d[i] +=1
        else:
            d[i] = 0
    d = sorted(d.items(),key = lambda x:-x[1])
    for i in d:
        answer.append(int(i[0]))
    return answer
    #return d
    


print(solution(s))
