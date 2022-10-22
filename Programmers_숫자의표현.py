def solution(n):
    answer = 1
    li = [i for i in range(n+1)]
    for i in range(1,n):
        tmp = li[i]
        idx = i
        while tmp <= n:
            if tmp == n:
                answer += 1
            tmp += li[idx+1]
            idx += 1
    return answer
print(solution(15))
