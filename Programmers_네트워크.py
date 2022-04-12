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
#내풀이->인접행렬 형식 보고 처음에 플루이드워셜로 시도

#BFS로 통과

# +
from collections import deque

computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
def bfs(start,graph,visited):
    q = deque()
    q.append(start)
    visited[start]=True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n)]
    visited=[False]*(n+1)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]==1:
                graph[i].append(j)

    for i in range(n):
        if visited[i] is False:
            bfs(i,graph,visited)
            answer += 1


    return answer

print(solution(n,computers))

# +
#아래가 77%통과한 클루이드 풀이//아마 한가지 연결만 찾아서 그런듯

# +

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3
INF = int(1e9)
    
def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] ==0:
                computers[i][j] = INF
    for k in range(n):
        for i in range(n):
            for j in range(n):
                computers[i][j] = min(computers[i][j],computers[i][k]+computers[k][j])
    for i in range(n):
        for j in range(i,n):
            if computers[i][j] == INF:
                answer += 1
    return computers
    if answer==0:
        return 1
    return answer

print(solution(n,computers))


# +
#고수의 풀이1_플루이드워셜
# -

def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))


# +
#고수의 풀이2_stack이용 dfs
# -

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

