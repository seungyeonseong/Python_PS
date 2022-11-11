import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    q = deque(list(map(int,input().split())))
    total = 0

    while q:
        tmp = max(q)
        x = q.popleft()
        m -= 1
        if x == tmp:
            total += 1
            if m <0:
                print(total)
                break
        else:
            q.append(x)
            if m <0:
                m = len(q)-1





