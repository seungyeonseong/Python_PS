import sys
import heapq
input = sys.stdin.readline


n = int(input())
li=[]
for _ in range(n):
    li.append(int(input()))

qmax, qmin =[],[]
for idx, i in enumerate(li):
    if len(qmin)==len(qmax):
        heapq.heappush(qmin,-i)
    else:
        heapq.heappush(qmax,i)
    if len(qmin) >=1 and len(qmax) >= 1 and qmin[0]*-1 > qmax[0]:
        minval = heapq.heappop(qmin)*-1
        maxval = heapq.heappop(qmax)
        heapq.heappush(qmin,maxval*-1)
        heapq.heappush(qmax,minval)
    print(qmin[0]*-1)

#진심 맞왜틀 풀이..ㅡㅡ
# mid = li[0]
# qmax = []
# qmin = []
#
# for idx,i in enumerate(li):
#     if idx == 0:
#         print(mid)
#         continue
#
#     elif mid < i and idx %2==0:
#         heapq.heappush(qmax,i)
#         tmp = heapq.heappop(qmax)
#         heapq.heappush(qmin,mid*-1)
#         mid = tmp
#
#     elif mid < i and idx %2==1:
#         heapq.heappush(qmax,i)
#     elif mid > i and idx%2==1:
#         heapq.heappush(qmin,-1*i)
#         tmp = heapq.heappop(qmin)*-1
#         heapq.heappush(qmax,mid)
#         mid = tmp
#     else:
#         heapq.heappush(qmin,-1*i)
#
#     print(mid)

