import sys
from collections import defaultdict

input = sys.stdin.readline


def game(li):
    mmin = int(1e9)
    mmax = 0
    for i in li.values():
        for j in range(len(i) - k + 1):
            x = i[j + k - 1] - i[j] + 1
            mmin = min(mmin, x)
            mmax = max(mmax, x)
    return (mmin, mmax)


t = int(input())
for _ in range(t):
    w = input().strip()
    k = int(input())
    li = defaultdict(list)
    for idx, i in enumerate(w):
        if w.count(i) >= k:
            li[i].append(idx)
    if not li:
        print(-1)
    else:
        print(*game(li))
