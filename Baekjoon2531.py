import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
sushi=[]
for _ in range(n):
    sushi.append(int(input()))

total = 0
sushi = sushi*2
for i in range(0,n):
    li = set(sushi[i:i+k])
    #print(len(li))
    if c in li:
        total = max(total,len(li))
    else:
        total = max(total,len(li)+1)

print(total)
