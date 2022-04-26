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
##칸이 비어서 옮길수없을때 continue로 처리
#->안해주니까 첨에 케이스 2개 런타임오류낫다
# -

def solution(board, moves):
    answer = 0
    li=[0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] !=0:
                break
        if j ==len(board)-1 and board[j][i-1]==0:
            continue

        if li[-1] == board[j][i-1]:
            li.pop()
            answer += 2
            board[j][i-1]=0
        else:
            li.append(board[j][i-1])
            board[j][i-1]=0


    return answer
