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
###구글링
#bfs로 풀이

# +
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    #q = deque()
    #q.append((x,y))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            if li[nx][ny] == 0:
                li[nx][ny] = li[x][y] + 1
                q.append((nx,ny))
                
    

m,n = map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))
res = 0
q= deque()
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            q.append((i,j))
tomato=True
            
bfs()
for i in li:
    for j in i:
        if j==0:
            tomato = False
        
    res = max(res,max(i))
    
if tomato is False:
    print(-1)
else:
    print(res-1)
            


# +
##내풀이_런타임에러남
#접근법:dfs이용
#틀린이유:깊이 들어갈 일이 없기 때문에 bfs써야함,,,,,무지해ㅠ,,

# +
def check(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny <0 or ny >=m:
            return False
        if li[nx][ny]==0:
            li[nx][ny] = 1
            check(nx,ny)
        elif li[nx][ny] == -1:
            return False
    return True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

m,n = map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

result = 0
for x in range(n):
    for y in range(m):
        if li[x][y] == 1:
            if check(x,y) == True:
                result += 1
print(result)

# -


