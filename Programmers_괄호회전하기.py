from collections import deque

def solution(s):
    answer = 0
    q = deque(list(s))
    for _ in range(len(s)):
        q.rotate()
        if check(q):
            answer +=1
    return answer

#올바른 문자열인지 확인하는 함수
def check(q):
    flag = True
    s = deque()
    for i in q:
        if not s:
            s.append(i)
            continue
        if i=="]" and s[-1]=="[":
            s.pop()
        elif i=="}" and s[-1]=="{":
            s.pop()
        elif i ==")" and s[-1]=="(":
            s.pop()
        else:
            s.append(i)
    if s:
        flag = False
    return flag