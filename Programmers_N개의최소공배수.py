arr = [2,6,8,14]
def solution(arr):
    if len(arr)==1:
        return arr[0]
    elif len(arr)==2:
        return lsm(arr[0],arr[1])
    else:
        answer = lsm(arr[0],arr[1])
        for i in range(2,len(arr)):
            answer = lsm(answer,arr[i])
        return answer

def lsm(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i

print(solution(arr))
