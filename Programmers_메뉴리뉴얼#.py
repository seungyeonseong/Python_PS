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
##n개의 단어쌍 구하기 -> 반복문으로 들어가 있는 개수 세기

# +
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer = []
    for k in course:
        temp = []
        for order in orders:
            for li in combinations(order,k):
                res = "".join(sorted(li))
                temp.append(res)
        sorted_candidates = Counter(temp).most_common()   #자료가 많은 순으로 정렬된 배열을 리턴하는 메서드             
        #print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt>1 and cnt == sorted_candidates[0][1]]
        
    return sorted(answer)
print(solution(orders,course))
# -


