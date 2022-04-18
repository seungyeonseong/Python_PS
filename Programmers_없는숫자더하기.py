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
def solution(numbers):
    li = [i for i in range(0,10)]
    answer = sum(li)

    for i in numbers:
        if i in li:
            answer -= i
    return answer

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))


# +
#이게맞지 ㅋㅋ
# -

def solution(numbers):
    return 45 - sum(numbers)
