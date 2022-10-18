# n = 7
# li = [[2,4],[11,4],[15,8],[4,6],[5,3],[8,10],[13,6]]
#내풀이_아래부터(가로 길이가 큰 면적부터) 더함.

import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))

ans = 0
def check(li,x):
    start,end = 0,0
    li = sorted(li,key=lambda x:x[0])
    for i in range(len(li)):
        if li[i][1] >= x:
            start = li[i][0]
            break
    for i in range(len(li)-1,-1,-1):
        if li[i][1] >= x:
            end = li[i][0]
            break
    return start,end+1
li = sorted(li,key = lambda x:(x[1],x[0]))
now = 0
for x,y in li:
    start,end = check(li,y)
    ans += (end-start)*(y-now)
    now = y


print(ans)

#남풀이


# m = 0
# m_idx = 0
# pli = [0 for _ in range(1001)] # 기둥
# for _ in range(int(input())):
#     L,H = map(int,input().split())
#     pli[L] = H
#     if m < H: # 가장 높은 기둥과 그 기둥의 인덱스를 찾음
#         m_idx = L
#         m = H
# curr = 0
# answer = 0
# for i in range(m_idx+1): # 왼쪽 그룹
#     curr = max(curr,pli[i])
#     answer += curr
# curr = 0
# for i in range(1000,m_idx,-1): # 오른쪽 그룹
#     curr = max(curr,pli[i])
#     answer += curr
# print(answer)

