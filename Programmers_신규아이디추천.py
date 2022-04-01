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
#가져갈 것:
#1.대문자->소문자***upper()/lower()
#2.특정문자 중복 제거***1)while+replace_2)split(".")
#3.맨 앞,뒤 특정 문자 제거***strip()

# +
new_id="...!@BaT#*..y.abcdefghijklm"


def solution(new_id):
    answer=""
    li=["-","_",".","1"]
    li += list("0123456789")
    new_id = new_id.lower()#1.대문자를 소문자로
    #알파벳,숫자,-,_,. 제외한 모든 문자 제거
    for i in new_id:
        if i.islower():
            answer += i
        elif i in li:
            answer +=i
    #마침표가 2번 이상 연속하면 하나로 치환
    while ".." in answer:
        answer = answer.replace("..",".")
    #마침표가 처음이나 끝에 있을 경우 제거
    answer = answer.strip(".")
    
    #빈 문자열일 경우 "a"대입
    if answer=="":
        answer = "a"
    #문자열 길이가 16자 이상일 경우, 첫 15개만
    if len(answer) >=16:
        answer = answer[0:15].strip(".")
    #길이가 2자 이하일 경우, 3이될때까지 마지막 문자 반복붙이기
    while len(answer)<3:
        answer += answer[-1]
    
    return answer
    
print(solution(new_id))

# +
#고수의 풀이_정규식,,,,메모,,

# +
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
