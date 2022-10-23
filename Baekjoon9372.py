#가중치가 1인 무향그래프
#모든 국가를 여행할 수 있다면 모두 연결되어있다는 뜻
# -> 최소신장트리:n-1개로 풀리는 어이없는 문제
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    n,m = map(int,input().split())
    res = 0
    graph=[[]for _ in range(n+1)]
    parent = [i for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            res += 1
    print(res)

