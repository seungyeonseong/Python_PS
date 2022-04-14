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
#최단 변환 개수 구하는 거니까 BFS로 시도,,,하고자만 함

#고수의 풀이
#단계별로 현재 선택한 단어와 한 글자 차이가 있는 알파벳만 모두 얻도록
#꺼내다가 target과 일치하는지 확인

# +
#가져갈 것
#zip함수: iterable 자료형이 개수가 동일할 때 사용

# +
def check(x,y):
    d = 0
    for i,j in zip(x,y):
        if i != j:
            d +=1
    if d==1:
        return True
    return False

def bfs(begin, target, words, visited):
    q = [(begin,0)]
    while q:
        cur,n = q.pop()
        if cur == target:
            return n
        for i in range(len(words)):
            if visited[i]:
                continue
            if check(cur,words[i]):
                visited[i] = True
                q.append((words[i],n+1))


def solution(begin, target,words):
    answer = 0
    if target not in words:
        return 0
    visited = [False]*(len(words))
    answer = bfs(begin, target, words, visited)

    return answer
