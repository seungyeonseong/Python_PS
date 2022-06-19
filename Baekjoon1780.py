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
#이분탐색
#정N각형 개수 찾기

# +
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))    
result = [0,0,0]    

def check(li,m,x,y):
    global result
    target = li[x][y]
    for i in range(x,x+m):
        for j in range(y,y+m):
            if li[i][j] != target:
                return False
    if target==-1:
        result[0] +=1
    elif target ==0:
        result[1] +=1
    else:
        result[2] +=1
    return True

def func(li,m,x,y):
    global result
    if m ==1:
        if li[x][y] ==-1:
            result[0] += 1
        elif li[x][y] == 0:
            result[1] += 1
        else:
            result[2] += 1
        return
        
    if check(li,m,x,y) is False:
        for i in range(3):
            for j in range(3):
                func(li,m//3,i*m//3+x,j*m//3+y)
            
func(li,n,0,0)
for i in result:
    print(i,end=" ")
                

# +
##내풀이__답은 맞는데 시간초과남,pypy로 했더니 메모리초과남ㅋ

#N이 3의 제곱이니까 탐색하다가 중간에 target과 다르면 9조각내야함
#9조각내지 않고 모든 범위를 돌면서 확인해서 시간초과나는듯

# +
#n = int(input())
#li=[]
#for _ in range(n):
#    li.append(list(map(int,input().split())))    
n=9
li = [[0, 0, 0, 1, 1, 1, -1, -1, -1],[0, 0, 0, 1, 1, 1, -1, -1, -1],[0, 0, 0, 1, 1, 1, -1, -1, -1],
      [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, -1, 0, 1, -1, 0, 1, -1],[0, -1, 1, 0, 1, -1, 0, 1, -1],[0, 1, -1, 1, 0, -1, 0, 1, -1]]
result = [0,0,0]    
def bin_search(li,m,x,y):
    global result
    target = li[x][y]
    if m ==1 and target==-1:
        result[0] += 1
        return
    elif m ==1 and target==0:
        result[1] += 1
        return
    elif m==1 and target ==1:
        result[2] += 1
        return
        
    
    for i in range(x,x+m):
        for j in range(y,y+m):
            if li[i][j] != target and m!=3:
                return bin_search(li,m-3,x,y)
            elif li[i][j] != target and m==3:
                return bin_search(li,1,x,y)
    if target ==-1:
        result[0] += 1
    elif target == 0:
        result[1]+= 1
    else:
        result[2] += 1
    for i in range(x,x+m):
        for j in range(y,y+m):
            li[i][j] = False
    return
    
for i in range(n):
    for j in range(n):
        if li[i][j] is not False:
            bin_search(li,min(n-i,n-j),i,j)
            

for i in result:
    print(i,end=" ")
                
