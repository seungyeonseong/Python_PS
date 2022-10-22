def solution(n):
    ans = 0
    return move(n,ans)

def move(n,ans):
    if n ==1:
        return ans +1
    if n%2==1:
        return move((n-1)//2,ans+1)
    else:
        return move(n//2,ans)