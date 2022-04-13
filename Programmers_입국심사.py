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
###이분탐색을 이용하는 정석풀이
#가장오래걸리는 시간을 high로 잡고 처리할 수 있는 인원구하기

# +
def solution(n,times):
    answer = 0
    left = 1
    right = max(times)*n
    while left < right:
        mid = (left+right)//2
        total = 0
        for t in times:
            total += mid//t
        if total >= n:
            right = mid
        else:
            left = mid+1
    answer = left
    return answer

print(solution(6,[7,10]))

# +
#테케만 맞고 0점맞은내풀이,,

# +

#대기시간+수행시간 고려해야함

import copy

def solution(n, times):
    answer = 0
    t_li = copy.deepcopy(times)
    #n -= len(times)
    while n>0: #모든 인원을 처리할 때까지 반복

        m = min(t_li)
        answer += m
        for i in range(len(t_li)):
            t_li[i] -= m

        wt=[]
        for i in range(len(t_li)):
            wt.append(t_li[i]+times[i])
        n_idx = wt.index(min(wt))
       # print(n_idx, t_li)
        if t_li[n_idx] !=0:
            for i in range(len(t_li)):
                if i == n_idx:
                    answer += t_li[n_idx]
                    t_li[n_idx] = times[n_idx]
                elif t_li[i] ==0:
                    continue
                else:
                    t_li[i] -= t_li[n_idx]
        else:
            t_li[n_idx] = times[n_idx]
        
        n -=1
        print(answer,n, t_li)   
        if n==0:
            return answer

print(solution(3,[1,2,3]))
