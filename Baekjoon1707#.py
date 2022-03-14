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
#이분그래프란, 인접한 정점끼리 서로 다른 색으로 칠해서 두 가지색으로만 칠할 수 있는 그래프

# +
###구글링
#1.DFS 풀이

# +
#import sys
#sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

def dfs(v,group):
    visited[v] = group    #방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0:    #아직 안가본 곳이면 방문
            if not dfs(i,-group):
                return False
        elif visited[i] == visited[v]: #방문한 곳인데, 그룹동일하면 False
            return False
    return True


for _ in range(int(input())):
    v,e = map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for _ in range(e):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    bipatite = True
    for i in range(1,v+1):
        if visited[i]==0:    #방문한 정점이 아니면 dfs수행
            bipatite = dfs(i,1)
            if not bipatite:
                break
                
    print("YES"if bipatite else "NO")
            

# +
###구글링
#2.BFS 풀이

# +
from collections import deque
#import sys
#input = sys.stdin.readline

for _ in range(int(input())):
    v,e = map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for _ in range(e):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque()
    group = 1
    bipatite = True
    for i in range(1,v+1):
        if visited[i]==0:    #방문한 정점이 아니면 bfs수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0:  #방문하지않은 정점이면 큐 삽입
                        q.append(w)
                        visited[w] = -1*visited[v]  #현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]:  #이미 방문한 경우, 동일한 그룹이면 False
                        bipatite = False
    
    print("YES"if bipatite else "NO")
            

# +
#내 개틀린 풀이

# +

tc = int(input())
for _ in range(tc):
    v,e = map(int,input().split())
    graph=[[] for _ in range(v+1)]
    arr=["WHITE"]*(v+1)
    res = "YES"
    for _ in range(e):
        x,y = map(int,input().split())
        if x<y:
            graph[x].append(y)
        else:
            graph[y].append(x)
        
    
    for i in range(1,v+1):
        if arr[i]=="WHITE" and len(graph[i])>0:
            arr[i] ="BLUE"
            
        if arr[i] == "BLUE":
            for j in range(len(graph[i])):
                if arr[j] == "BLUE":
                    res = "NO"
                    break
                arr[j] = "RED"
        else:
            for j in range(len(graph[i])):
                if arr[j] == "RED":
                    res = "NO"
                    break
                arr[j] = "BLUE"

        
    print(res)
