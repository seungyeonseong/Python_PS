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
#1트에 이중 for문 구현했더니 효율성테스트 시간초과
# 1)정렬 2)한 줄 for문으로 해결 

# +
phone_book=["12","123","1235","567","88"]

def solution(phone_book):
    answer = True
   
    phone_book.sort(key = lambda x:x)
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer

print(solution(phone_book))


# +
#고수의 풀이
# -

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
