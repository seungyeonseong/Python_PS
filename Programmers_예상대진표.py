import math

def solution(n,a,b):
    answer = math.log2(n)
    step = n//2
    if a >b:
        a,b = b,a
    while True:
        if b > step and a<= step :
            return answer
        elif b <= step:
            step -= 2**(answer-2)
        elif b > step:
            step += 2**(answer-2)
        answer -=1
    # return answer