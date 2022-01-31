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
from collections import deque

#dfs 프로그램 작성_재귀함수이용
def dfs(graph,v,visited):
    #시작부분 방문처리
    visited[v] = True
    print(v, end=" ")
    #해당 노드와 연결된 노드 중 가장 작은 것 
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph,i,visited)

#bfs 프로그램 작성_큐 이용
def bfs(graph,v,visited):
    queue = deque([v])    #시작노드를 큐에 삽입하고 
    visited[v] = True    #방문처리
    while queue:
        v = queue.popleft()  #큐에서 노드를 꺼내
        print(v,end=" ")
       
        for i in graph[v]:
            if visited[i] is False:
                queue.append(i) 
                visited[i] = True  
    






#입력    
n, m, v = map(int,input().split())
visited = [False]*(n+1)

#인접 리스트 방식
graph = [[] for _ in range(n+1) ]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) #######양방향이므로 둘다 넣어줘야함!!!
#정렬
for i in range(1,n+1):
    graph[i].sort()
            
dfs(graph,v,visited)
print()
visited = [False]*(n+1)
bfs(graph,v,visited)
            
# -


