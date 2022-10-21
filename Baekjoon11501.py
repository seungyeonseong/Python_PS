import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n =int(input())
    li = list(map(int,input().split()))
    m,res = 0,0

    for i in range(n-1,-1,-1):
        if li[i] > m:
            m = li[i]
        else:
            res += m-li[i]
    print(res)

#틀린풀이
# from collections import deque
# q = deque()
# res = 0
#
# for i in range(n):
#     if len(q)==0:
#         q.append(li[i])
#     else:
#         if q[-1] > li[i]:
#             x = q.pop()
#             while q:
#                 y = q.popleft()
#                 res += x-y
#             q.append(li[i])
#         else:
#             q.append(li[i])
#     print(q)
# if len(q) >1:
#     x = q.pop()
#     while q:
#         y = q.popleft()
#         res += x-y
# print(res)