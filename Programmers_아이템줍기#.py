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

# #아이디어
# 1. 최종 테두리만 남기기
# -> 다른 직사각형안에 완전히 포함되는 케이스는 없는데 있다고 생각해서 구현x,,,조건읽기
#
# 2. bfs최단경로 계산

# #가져갈 것
# 1. 최단경로 구할 때 모서리가 겹쳐지면 잘못된 경로로 이동할 수 있다!
# => 2차원 그래프 배열 2배로 늘리기 

# +
rectangle= [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX, characterY, itemX, itemY = 1,3,7,8

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0 
    graph =[[0]*101 for _ in range(101)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    #테두리+내부 1로 채우기
    for x1,y1,x2,y2 in rectangle:
        for i in range(2*x1,2*x2+1):
            for j in range(2*y1,2*y2+1):
                graph[i][j] = 1
    #내부 0으로 채우기
    for x1,y1,x2,y2 in rectangle:
        for i in range(2*x1+1,2*x2):
            for j in range(2*y1+1,2*y2):
                graph[i][j] = 0    
                
    #최단 경로 구하기
    q = deque()
    q.append((characterX,characterY))
    graph[characterX][characterY] = 0
    answer = 0
    while q:
        x,y = q.popleft()
        if x==itemX and y== itemY:
            answer = (graph[x][y] )//2
            break
            
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0 <=nx <101 and  0<=ny<101 and graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+ 1
                q.append((nx,ny))
    return answer
    

print(solution(rectangle, characterX, characterY, itemX, itemY))

