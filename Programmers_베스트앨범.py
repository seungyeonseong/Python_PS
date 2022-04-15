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
#genres =["classic", "pop", "classic", "classic", "pop"]
#plays = [500, 600, 150, 800, 2500]
def solution(genres, plays):
    answer = []
    d = dict()
    for i in set(genres):
        d[i]= 0
        for j in range(len(plays)):
            if genres[j] == i:
                d[i] += plays[j]
    d = sorted(d.items(),key = lambda x:x[1],reverse=True)
    print(d)
    
    for i in d:
        li=[]
        for n,j in enumerate(plays):
            if i[0]== genres[n]:
                li.append((j,n))
        if len(li) == 1:
            answer.append(li[0][1])
            continue
        li.sort(key = lambda x:x[0],reverse = True)

        for n in range(2):
            answer.append(li[n][1])

    return answer


print(solution(['A', 'B', 'A', 'A', 'B'], [
      500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B'], [500]) == [0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
