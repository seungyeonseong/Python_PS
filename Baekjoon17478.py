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
N = int(input())
def func(n,N):
    if n ==N:
        print("_"*4*n +"\"재귀함수가 뭔가요?\"")
        print("_"*4*n +"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print("_"*4*n +"라고 답변하였지.")
        return
    
    print("_"*4*n +"\"재귀함수가 뭔가요?\"")
    print("_"*4*n +"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print("_"*4*n +"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("_"*4*n +"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"") 
    func(n+1,N)
    print("_"*4*n +"라고 답변하였지.")
 
         
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
func(0,N)
#for i in range(N-1,-1,-1):
#print("-"*4*i + "라고 답변하였지.")
