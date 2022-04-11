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

#고수의 풀이
#왼쪽,오른쪽 방향전환하는 함수 구현 실패


# +
name = "JEROEN"
def solution(name):

    answer = 0
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
                      next += 1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - nxt, i + 2 * (len(name) -nxt)])
        
    answer += min_move
    return answer
                      

print(solution(name))

# +
#왜틀리는지모를,,,내풀이

# +
#name = "JEROEN"
#name = "JAN"
name = "ABAAAAAAAAABB" #10900



def solution(name):
    answer = 0
    #A부터 셀건지, Z부터 셀건지
    alpha = [min(ord(i)-ord("A"),ord("Z")-ord(i)+1) for i in name]
    
    i = 0
    while True:

        answer += alpha[i]
        alpha[i] = 0  
        
        if sum(alpha) == 0:
            return answer
        
        left, right = 1,1
        while alpha[i-left]==0:
            left +=1
        while alpha[i+right]==0:
            right +=1
        if right >left:
            answer += left
            i -= left
        else:
            answer +=right
            i += right
    

print(solution(name))
