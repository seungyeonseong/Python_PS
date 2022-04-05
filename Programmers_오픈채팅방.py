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
##내풀이->딕셔너리 ,,고수의 풀이와 비슷하게 접근함,,!

# +
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    answer = []
    #가장 최근 닉네임으로 설정
    nickname={}
    for i in record:
        x = i.split(" ")
        if len(x) ==3:
            nickname[x[1]] = x[2]
    for i in record:
        x = i.split(" ")
        if x[0] == "Enter":
            answer.append(nickname[x[1]]+"님이 들어왔습니다.")
        elif x[0] =="Leave":
            answer.append(nickname[x[1]]+"님이 나갔습니다.")
    
    return answer

print(solution(record))


