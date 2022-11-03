import sys
input = sys.stdin.readline

k = int(input())
li = list(map(int,input().split()))
total =[[] for _ in range(k+1)]
def sol(l,k):
  if k ==2:
    total[1].append(l[0])
    total[2].append(l[1])
    total[1].append(l[2])
    return
  total[k].append(l[2**(k-1)-1])
  sol(l[:2**(k-1)-1],k-1)
  sol(l[2**(k-1):],k-1)

sol(li,k)
for i in range(k,0,-1):
  print(*total[i])

