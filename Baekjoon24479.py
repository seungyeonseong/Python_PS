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
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited =[False]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
num  = 1  

res =[[] for _ in range(n+1)]   
def dfs(start):
    global num
    res[start] = num
    visited[start] = True
    for i in sorted(graph[start]):
        if visited[i] is False:
            num +=1
            dfs(i)
            
dfs(r)
#res = sorted(res,key = lambda x:x[0])
for i in range(1,n+1):
    if visited[i] is False:
        print(0)
    else:
        print(res[i])

