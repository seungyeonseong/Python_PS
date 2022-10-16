import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = dict()
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in d:
        d[word][0] += 1
    else:
        d[word] = [1,len(word),word]

d = sorted(d.values(),key=lambda x:(-x[0],-x[1],x[2]))
for i in d:
    print(i[2])