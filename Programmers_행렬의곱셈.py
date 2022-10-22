def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        li =[]
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[i])):
                tmp += arr1[i][k]*arr2[k][j]
            li.append(tmp)
        answer.append(li)
    return answer