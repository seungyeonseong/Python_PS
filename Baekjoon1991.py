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
#왜 자꾸 끝에 None이붙는지 몰겟다,,,,,그래서 무식하게 풀음

# +
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    x,a,b = input().split()
    if a==".":
        a = None
    if b ==".":
        b = None
        
    graph[ord(x)-65].append(a)
    graph[ord(x)-65].append(b)
def inorder(start,graph,li):
    if graph[ord(start)-65][0] != None:
        inorder(graph[ord(start)-65][0],graph,li)
    li.append(start)
    if graph[ord(start)-65][1] != None:
        inorder(graph[ord(start)-65][1],graph,li)
        
def preorder(start,graph,li):
    print(start,end="")
    if graph[ord(start)-65][0] != None:
        preorder(graph[ord(start)-65][0],graph,li)
    if graph[ord(start)-65][1] != None:
        preorder(graph[ord(start)-65][1],graph,li)
        
def postorder(start,graph,li):
    if graph[ord(start)-65][0] != None:
        postorder(graph[ord(start)-65][0],graph,li)
    if graph[ord(start)-65][1] != None:
        postorder(graph[ord(start)-65][1],graph,li)
    print(start,end="")
    
li=[]
preorder('A',graph,li)
print("".join(li))
li=[]
inorder('A',graph,li)
print("".join(li))
li=[]
postorder('A',graph,li)
print("".join(li))


# +
#None붙는 풀이

# +
import sys
input =sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    x,a,b = input().split()
    graph[ord(x)-65].append(a)
    graph[ord(x)-65].append(b)
def inorder(start,graph):

    if graph[ord(start)-65][0] != ".":
        inorder(graph[ord(start)-65][0],graph)
    if start is not None:
        print(start,end="")
    else:
        return
    if graph[ord(start)-65][1] != ".":
        inorder(graph[ord(start)-65][1],graph)
        
def preorder(start,graph):
    print(start,end="")
    if graph[ord(start)-65][0] != ".":
        preorder(graph[ord(start)-65][0],graph)
    if graph[ord(start)-65][1] != ".":
        preorder(graph[ord(start)-65][1],graph)
        
def postorder(start,graph):
    if graph[ord(start)-65][0] != ".":
        postorder(graph[ord(start)-65][0],graph)
    if graph[ord(start)-65][1] != ".":
        postorder(graph[ord(start)-65][1],graph)
    print(start,end="")

print(preorder('A',graph))
print(inorder('A',graph))
print(postorder('A',graph))

