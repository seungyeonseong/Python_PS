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
#문제 이해가 어렵고 구현은 괜찮,,

# +
from collections import deque
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def check(p,idx):
    li=[]
    for j in places[idx]:
        li.append(list(j))
    q = deque()
    for i in range(5):
        for j in range(5):
            if li[i][j]=="O":
                q.append((i,j))
    while q:
        x,y = q.pop()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0<=ny<5 and li[nx][ny]=="P":
                cnt += 1
        if cnt >=2:
            return 0
    for i in range(5):
        for j in range(5):
            if li[i][j] =="P":
                q.append((i,j))
                    
    while q:
        x,y = q.pop()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and li[nx][ny]=="P":
                return 0
    return 1
                    
def solution(places):
    answer = []
    for idx in range(5):
        answer.append(check(p,idx)) 
    
    return answer

print(solution(places))
