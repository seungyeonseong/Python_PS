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
#구글링

#{시작점:[도착점],...} 형태의 인접 그래프 생성
#도착점 리스트 정렬
#dfs 알고리즘 사용=>스택이 빌때까지
#1.스택에서 가장 위 데이터(top) 가져옴
#2.top이 그래프에 없거나, 티켓을 모두 사용한 경우 path에 저장
#3.그 외엔 top을 시작점으로 하는 도착데이터 중 가장 앞 데이터를 stack에 저장
#4.path를 역순으로 출력

# +
from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list) #디폴트값이 list인 딕셔너리
    
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    
    for key in routes.keys():
        routes[key].sort(reverse = True)
        
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
        
    return answer    


# -

# BFS로 풀려고 시도했는데 아래 케이스 예외처리하는 코드 구현 못함+고수들의 BFS풀이 이해 못함,,,ㅜ =>50점맞은 내풀이

# +
from collections import deque

def solution(tickets):
    answer = ["ICN"]
    tickets.sort(key = lambda x:x[1])
    q = deque(tickets)
    now = "ICN"
    
    
    while q:
        x,y = q.popleft()
        if x == now:
            for i in tickets:
                if i[1] == y:
                    answer.append(y)
                    now = y
                    break
            q.append((x,y))

        else:
            q.append((x,y))
        
    return answer

tickets =[['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]

print(solution(tickets))
# -

#옛날 풀이-->50점
'''def solution(tickets):
    answer=[]
    answer.append("ICN")
    tickets.sort(key = lambda x:x[1])
    visited = [0]*(len(tickets))
    
    while sum(visited) != len(tickets):
        for i in range(len(tickets)):
            if tickets[i][0] == answer[-1] and visited[i] == 0:
                answer.append(tickets[i][1])
                visited[i] = 1
    
    return answer
'''
