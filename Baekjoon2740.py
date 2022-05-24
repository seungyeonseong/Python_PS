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
n,m =map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
m,k = map(int,input().split())
B=[]
for _ in range(m):
    B.append(list(map(int,input().split())))

n,m = 3,2
A =[[1,2],[3,4],[5,6]]
m,k = 2,3
B = [[-1,-2,0],[0,0,3]]
res=[]
for i in range(n):
    li=[]
    for j in range(k):
        
        x = 0
        for e in range(m):
            x += A[i][e]*B[e][j]
        print(x,end=" ")
    print("")
    
#print(res)
