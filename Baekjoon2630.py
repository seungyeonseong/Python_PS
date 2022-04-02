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
##divde-and-conquer
#재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄이는 방식

# +
import sys
input = sys.stdin.readline

n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
blue,white = 0,0

    
def func(x,y,N):
    color = graph[x][y]
    global blue
    global white
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != graph[i][j]:
                func(x,y,N//2)
                func(x,y+N//2,N//2)
                func(x+N//2,y,N//2)
                func(x+N//2,y+N//2,N//2)
                return
    if color ==0:
        white +=1
    else:
        blue +=1
        
func(0,0,n)
print(white)
print(blue)
    
# -


