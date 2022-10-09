import sys
input = sys.stdin.readline

n,l = map(int,input().split())
li=[]
#웅덩이 표시
for _ in range(n):
    li.append(list(map(int,input().split())))
li = sorted(li,key= lambda x:x[0])
now = li[0][0]

total = 0
for start,end in li:
    if now > start:
        start = now

    if (end-start)%l==0: #크기가 딱 맞을때
        total += (end-start)//l
        continue
    else:
        x = (end-start)//l
        total += 1
        total += x
        now = start + (x+1)*l

print(total)


