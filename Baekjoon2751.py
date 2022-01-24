
import sys

#정수를 받을때
n = int(sys.stdin.readline())
#여러개의 정수들을 받을 때
data = [int(sys.stdin.readline()) for i in range(n)]
#print(data)

#정렬
data.sort()
for i in data:
    print(i)