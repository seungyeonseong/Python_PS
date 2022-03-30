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
##시간초과남-->91점 풀이
# -

def solution(id_list, report, k):
    #answer = []
    report =set(report)
    li=[]
    for i in report:
        li.append(i.split())
    #print(li)

    num=[[] for _ in range(len(id_list))]
    for i in li:
        for j in range(len(id_list)):
            if i[0]==id_list[j]:
                num[j].append(i[1])
    #print(num)
    blacklist=[]
    for name in id_list:
        total = 0
        for i in range(len(num)):
            if name in num[i]:
                total +=1
        if total >=k:
            blacklist.append(name)
    #print(blacklist)

    answer=[0]*(len(id_list))
    for i in range(len(num)):
        for j in blacklist:
            if j in num[i]:
                answer[i] += 1
    #print(mail)
    return answer


# +
###구글링***
#가져갈 것
#1.딕셔너리 사용
#2.set으로 중복 제거

# +
#id가 신고한 목록/id를 신고한 목록을 따로 저장
from collections import defaultdict

def solution(id_list,report,k):
    report = set(report)
    answer = []
    count = defaultdict(int) #몇번신고했는지
    user = defaultdict(set) #신고 리스트
    
    #1. 누가 누구를 신고했는지 dict담기 &신고당한 횟수 세기
    for r in report:
        a,b = r.split()
        user[a].add(b)
        count[b] += 1
    #2. 이용자별로 자신이 신고한 사람이 k번 이상이라면 처리된 횟수 +1
    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result +=1
        answer.append(result)
    return answer
