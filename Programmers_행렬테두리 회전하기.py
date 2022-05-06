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
##진심 머리터지는줄,,간단한데 tmp에 담아옮기는 과정에서 뭘 놓쳤는지 틀림
#구글링의 도움을 받은 풀이 

# +
import copy 
def solution(rows, columns, queries):
    answer = []
    #1.행렬만들기
    graph=[[0]*(columns+1) for _ in range(rows+1)]
    n = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            graph[i][j] = n
            n += 1
            
    #2. for문으로 4번 우하좌상순으로 값교체
    for change in queries:
        x1,y1,x2,y2 = change
        tmp = copy.deepcopy(graph[x1][y1])
        num = tmp
        #상
        for k in range(x1,x2):
            test = graph[k+1][y1]
            graph[k][y1] = test
            tmp = min(tmp,test)

        for k in range(y1,y2):
            test = graph[x2][k+1]
            graph[x2][k] = test
            tmp = min(tmp, test)

        for k in range(x2,x1,-1):
            test = graph[k-1][y2]
            graph[k][y2] = test
            tmp = min(tmp, test)

        for k in range(y2,y1,-1):
            test = graph[x1][k-1]
            graph[x1][k] = test
            tmp = min(tmp, test)
            
        graph[x1][y1+1] = num
        answer.append(tmp)
    return answer

queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
rows, columns = 6,6
print(solution(rows,columns,queries))

# +
#이게 빙글빙글내풀이

# +
import copy 
def solution(rows, columns, queries):
    answer = []
    #1.행렬만들기
    graph=[[0]*(columns+1) for _ in range(rows+1)]
    n = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            graph[i][j] = n
            n += 1
            
    #2. for문으로 4번 우하좌상순으로 값교체
    for change in queries:
        x1,y1,x2,y2 = change
        m = copy.deepcopy(graph[x1][y1])
        #우
        for j in range(y1,y2+1):
            before = graph[x1][j]
            if j==y2:
                break
            graph[x1][j+1] = graph[x1][j]
            if m > graph[x1][j]:
                m = graph[x1][j]
    #하
        graph[x1+1][y2] = before
        for i in range(x1+1,x2+1):
            before = graph[i][y2]
            if i==x2:
                break
            graph[i+1][y2] = graph[i][y2]
            if m > before:
                m = before
    #좌
        graph[x2][y2-1] = before
        for j in range(y2-2,y1-1,-1):
            before = graph[x2][j]
            if j==y1:
                break
            graph[x2][j-1] = graph[x2][j]
            if m > before:
                m = before
    #상
        graph[x2-1][y1] = before
        for i in range(x2-2,x1-1,-1):
            before = graph[i][y1]
            graph[i-1][y1] = graph[i][y1]
            if m > before:
                m = before
        answer.append(m)
    #3. 최솟값 저장해서 answer에 넣기
    #return graph
    return answer

queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
rows, columns = 6,6
print(solution(rows,columns,queries))
