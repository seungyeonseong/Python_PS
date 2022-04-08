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

#이게왜되지...
#가져갈 것->1)enumerate함수 2)any함수


# +
from collections import deque

priorities=[2, 1, 3, 2]
location=2

def solution(priorities, location):
    answer = 0
    res=[]
    arr=deque() #순서대로 배열에 넣기
    for i in range(len(priorities)):
        arr.append((priorities[i],i+1))
    while arr:
        num = len(arr)
#인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        x,y = arr.popleft() 
        for i in arr:
            if x < i[0]:
#나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
                arr.append((x,y)) 
                break
     
        if len(arr) !=num:
            res.append(y)   #그렇지 않으면 J를 인쇄합니다.
    answer = res.index(location+1)
    return answer+1
    

print(solution(priorities,location))


# +
#고수의 풀이
# -

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
