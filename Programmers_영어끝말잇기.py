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

def solution(n, words):
    answer = [0,0]
    li=[]
    words = [words[0][0]]+words
    print(words)
    last = words[0]
    for idx,word in enumerate(words):
        if idx==0:
            continue
        if len(word)<2:
            return [0,0]
        if word[0] != last or word in li:
            if idx%n==0:
                answer[0] = n
                answer[1] = idx//n
            else:
                answer[0] = idx%n
                answer[1] = idx//n+1
            return answer
        li.append(word)
        last = word[-1]
    return answer
