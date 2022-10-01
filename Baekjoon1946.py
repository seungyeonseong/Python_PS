import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        score.append(list(map(int,input().split())))
    total = 1
    score = sorted(score,key =lambda x:x[0])
    tmp = score[0][1]

    for i in range(1,N):
        if score[i][1] < tmp:
            total += 1
            tmp = score[i][1]
    print(total)

